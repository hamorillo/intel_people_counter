#!/usr/bin/env python3
"""
 Copyright (c) 2018 Intel Corporation.

 Permission is hereby granted, free of charge, to any person obtaining
 a copy of this software and associated documentation files (the
 "Software"), to deal in the Software without restriction, including
 without limitation the rights to use, copy, modify, merge, publish,
 distribute, sublicense, and/or sell copies of the Software, and to
 permit persons to whom the Software is furnished to do so, subject to
 the following conditions:

 The above copyright notice and this permission notice shall be
 included in all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
 LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
 OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
 WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import os
import sys
import logging as log
from openvino.inference_engine import IENetwork, IECore


class Network:
    """
    Load and configure inference plugins for the specified target devices 
    and performs synchronous and asynchronous modes for the specified infer requests.
    """

    def __init__(self):
        self.plugin = None
        self.network = None
        self.exec_network = None
        self.input_blob = None
        self.output_blob = None

    def load_model(self, model, device="CPU", cpu_extension=None):

        model_xml = model
        model_bin = os.path.splitext(model_xml)[0] + ".bin"

        # Inference Engine initialization
        self.plugin = IECore()

        # Read the IR as a IENetwork
        self.network = IENetwork(model=model_xml, weights=model_bin)

        ### TODO: Check for supported layers ###
        supported_layers = self.plugin.query_network(
            network=self.network, device_name="CPU")

        unsupported_layers = [
            l for l in self.network.layers.keys() if l not in supported_layers]
        if len(unsupported_layers) != 0:
            print("Unsupported layers found: {}".format(unsupported_layers))
            print("Check whether extensions are available to add to IECore.")
            exit(1)

        # Add extension if it has been especified and we are executing in that device
        if cpu_extension and "CPU" in device:
            self.plugin.add_extension(cpu_extension, device)

        # Load the IENetwork (model) into the plugin
        self.exec_network = self.plugin.load_network(self.network, device)

        # Get the input layer
        self.input_blob = next(iter(self.network.inputs))
        self.output_blob = next(iter(self.network.outputs))

        ### TODO: Return the loaded inference plugin ###
        return self.plugin

    def get_input_shape(self):
        ### TODO: Return the shape of the input layer ###
        return self.network.inputs[self.input_blob].shape

    def get_output_shape(self):
        return self.network.outputs[self.output_blob].shape

    def exec_net(self, image):
        ### TODO: Start an asynchronous request ###
        ### TODO: Return any necessary information ###
        ### Note: You may need to update the function parameters. ###
        self.infer_request = self.exec_network.start_async(
            request_id=0, inputs={self.input_blob: image})
        return

    def wait(self):
        ### TODO: Wait for the request to be complete. ###
        ### TODO: Return any necessary information ###
        ### Note: You may need to update the function parameters. ###
        status = self.infer_request.wait(-1)
        return status

    def get_output(self):
        # TODO: Extract and return the output results
        ### Note: You may need to update the function parameters. ###
        time_infering = 0
        for key, value in self.infer_request.get_perf_counts().items():
            time_infering += value['real_time']

        log.debug('Time infering:' + str(self.infer_request.latency) + ' ms')
        return self.infer_request.outputs[self.output_blob], self.infer_request.latency
