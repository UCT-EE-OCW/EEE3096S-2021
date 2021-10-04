//Define the module
module ALU(
    input clk,A,B,
    input [1:0] ALU_Sel,
    output reg ALU_out
);

reg ALU_result;

always@(posedge clk) //Triggered on rising edge clock
    begin
        case(ALU_Sel)
            2'b00:  //Manually enumerate Addition = 00
                ALU_result = A + B;
            
            2'b01:  //Manually enumerate Subtraction1 = 01
                ALU_result = A - B;

            2'b10:  //Manually enumerate Subtraction2 = 10
                ALU_result = B - A;
            
            2'b11:  //Manually enumerate Multiplication = 11
                ALU_result = A * B;
            default: ALU_result = A;
        endcase

        ALU_out <= ALU_result;
    end    
endmodule