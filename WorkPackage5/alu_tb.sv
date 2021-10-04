//Define the ALU testbench module
module ALU_tb();    
//inputs
reg clk, A,B;
reg[1:0] ALU_Sel;
// output
wire ALU_Out; 

//Instantiate the design under test
ALU dut(
    .clk(clk),
    .A(A),
    .B(B),
    .ALU_Sel(ALU_Sel),
    .ALU_out(ALU_Out));

initial begin //Initial means this only happens once
    $display("A  B  ALU_Sel  ALU_Out");
    $monitor("%b  %b  %b     %b",A,B,ALU_Sel, ALU_Out);
    clk = 1'b1;
    A = 1'b1;
    B = 1'b1;
    ALU_Sel = 2'b0;
    #5  //Note: This is not synthesizable and only available in simulation
        clk=!clk;
    #5
        clk=!clk;
        ALU_Sel = 2'b01;
    #5
        clk=!clk;
    #5
        clk=!clk;
        ALU_Sel = 2'b10;
    #5
        clk=!clk;
    #5
        clk=!clk;
        ALU_Sel = 2'b11;
    #5
        clk = !clk;
    end
endmodule