`timescale 1ns / 1ps

module reg_mem (addr, data_in, wen, clk, data_out);

    parameter DATA_WIDTH = 8; //8 bit wide data
    parameter ADDR_BITS = 5; //32 Addresses

    input [ADDR_BITS-1:0] addr;
    input [DATA_WIDTH-1:0] data_in;
    input wen;
    input clk;
    output [DATA_WIDTH-1:0] data_out;

    reg [DATA_WIDTH-1:0] data_out;

    //8 memory locations each storing a 4bits wide value
    reg [DATA_WIDTH-1:0] mem_array [(2**ADDR_BITS)-1:0];

    always @(posedge clk) begin

        if (wen) begin //Write
            mem_array [addr] <= data_in;
            data_out <= #(DATA_WIDTH)'b0;
        end

        else begin //Read
            data_out <= mem_array[addr];
        end
    end

endmodule
