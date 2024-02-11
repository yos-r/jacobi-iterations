from manim import *
import sympy as sp
from manim import config as global_config
class Jacobi(Scene):
    title=Title("Méthode de Jacobi").set_color(BLUE_E)
    adjustedA= Matrix([[1,"1\over 2","1\over 2"],
                       ["1\over 2",1,"1\over 2"]
                       ,["1\over 2","1\over 2",1]]
                      ,element_alignment_corner=[0, 0, 0.5],
                      v_buff=1.3)
    A=Matrix([[4,1,1],[1,4,1],[1,1,4]],v_buff=1.3)
    B=Matrix([[6],[6],[6]],v_buff=1.3)
    matA=MathTex('A')
    matB=MathTex('B')
    
    AB=VGroup().add(matA,matB,A,B).arrange_in_grid(cols=2,rows=2,buff=MED_LARGE_BUFF).scale(0.8)
    
    X_6=Matrix([["63\over 64"],["63\over 64"],["63\over 64"]],v_buff=1.3).scale(0.7)    
    mat_X_6=MathTex("X^{(6)}").set_color(YELLOW).scale(0.8)
    X6=VGroup().add(mat_X_6,X_6).arrange(DOWN,0.5)
    
    X_5=Matrix([["33\over 32"],["33\over 32"],["33\over 32"]],v_buff=1.3).scale(0.7)    
    mat_X_5=MathTex("X^{(5)}").set_color(YELLOW).scale(0.8)
    X5=VGroup().add(mat_X_5,X_5).arrange(DOWN,0.5)
    
    X_4=Matrix([["15\over 16"],["15\over 16"],["15\over 16"]],v_buff=1.3).scale(0.7)    
    mat_X_4=MathTex("X^{(4)}").set_color(YELLOW).scale(0.8)
    X4=VGroup().add(mat_X_4,X_4).arrange(DOWN,0.5)
    
    X_3=Matrix([["9\over 8"],["9\over 8"],["9\over 8"]],v_buff=1.3).scale(0.7)    
    mat_X_3=MathTex("X^{(3)}").set_color(YELLOW).scale(0.8)
    X3=VGroup().add(mat_X_3,X_3).arrange(DOWN,0.5)
    
    X_2=Matrix([["3\over 4"],["3\over 4"],["3\over 4"]],v_buff=1.3).scale(0.7)    
    mat_X_2=MathTex("X^{(2)}").set_color(YELLOW).scale(0.8)
    X2=VGroup().add(mat_X_2,X_2).arrange(DOWN,0.5)
    
    X_1=Matrix([["3\over 2"],["3\over 2"],["3\over 2"]],v_buff=1.3).scale(0.7) 
    mat_X_1=MathTex("X^{(1)}").set_color(YELLOW).scale(0.8)
    X1=VGroup().add(mat_X_1,X_1).arrange(DOWN,0.5)
    
    X_0=Matrix([[0],[0],[0]],v_buff=1.3,element_alignment_corner=[0, 0, 0.5])    
    mat_X_0=MathTex("X^{(0)}").set_color(YELLOW)
    X0=VGroup().add(mat_X_0,X_0).arrange(DOWN,0.5).scale(0.8)
    
    X=VGroup().add(X4,X3,X2,X1,X0)
    todo=VGroup().add(AB,X).arrange(RIGHT,0.5).next_to(title,2*DOWN)
    

    equation=MathTex(r"x^{(k+1)}_{i} = \frac{b _{i}-\sum_{\scriptstyle\substack{ j =1 \\ j \neq i }}^n a_{i j}x^{(k)}_{i}}{a_{ii}}")
    equation.align_on_border(DOWN)
    
    def construct(self):
        config.max_files_cached=-1
        
        self.subscene1()
    def subscene1(self):
        self.add(self.title,self.equation,self.AB)
        pivot=SurroundingRectangle(self.A.get_rows()[0][0], color=YELLOW_E)
        b= SurroundingRectangle(self.B.get_columns()[0][0], color=YELLOW_E)
        self.play(Write(self.X0))
        self.wait(2)
        self.play(self.X0.animate.shift(RIGHT))
        xi= VGroup().add(SurroundingRectangle(self.X_0.get_columns()[0][1],color=BLUE_E),SurroundingRectangle(self.X_0.get_columns()[0][2],color=BLUE_E))
        ai=VGroup().add(SurroundingRectangle(self.A.get_rows()[0][1],color=BLUE_E),SurroundingRectangle(self.A.get_rows()[0][2],color=BLUE_E))
        
        self.X1.next_to(self.X0,LEFT)
        self.X_1.get_columns().set_color(BLACK)
        self.play(Write(self.X1))
        
        x=SurroundingRectangle(self.X_1.get_columns()[0][0], color=PURPLE)
        
        self.play(Write(x),Transform(self.equation,MathTex(r"x^{(1)}_1 = \frac{b_1 - a_{12}x_{2}^{(0)} - a_{13}x_{3}^{(0)}}{a_{11}}").move_to(self.equation)))
        self.play(Write(pivot),Write(b),Write(xi),Write(ai))
        self.play(Transform(self.equation,MathTex(r"x^{(1)}_1 = \frac{6 - 0- 0}{4}=\frac{3}{2}").move_to(self.equation)))
        self.play(self.X_1.get_columns()[0][0].animate.set_color(WHITE))
        self.wait(1)
        #transform parsers
        self.play(Transform(x,SurroundingRectangle(self.X_1.get_columns()[0][1],color=PURPLE)),
                  Transform(self.equation,MathTex(r"x^{(1)}_2 = \frac{b_2 - a_{21}x_{1}^{(0)} - a_{23}x_{3}^{(0)}}{a_{22}}").move_to(self.equation)),
        )
        # self.wait(1)
        self.play(Transform(pivot,SurroundingRectangle(self.A.get_rows()[1][1],color=YELLOW_E)),
                  Transform(b,SurroundingRectangle(self.B.get_rows()[1][0],color=YELLOW_E)),
                  Transform(ai,VGroup().add(SurroundingRectangle(self.A.get_rows()[1][0],color=BLUE_E),SurroundingRectangle(self.A.get_rows()[1][2],color=BLUE_E))),
                  Transform(xi,VGroup().add(SurroundingRectangle(self.X_0.get_columns()[0][0],color=BLUE_E),SurroundingRectangle(self.X_0.get_columns()[0][2],color=BLUE_E)))
                  )
        #write out new eq
        self.wait(1)
        self.play(Transform(self.equation,MathTex(r"x^{(1)}_2 = \frac{6 - 0- 0}{4}=\frac{3}{2}").move_to(self.equation)))
        # reveal result
        self.play(self.X_1.get_columns()[0][1].animate.set_color(WHITE))
        self.wait(1)
        
        self.play(Transform(x,SurroundingRectangle(self.X_1.get_columns()[0][2],color=PURPLE)),
                  Transform(self.equation,MathTex(r"x^{(1)}_3 = \frac{b_3 - a_{31}x_{1}^{(0)} - a_{32}x_{2}^{(0)}}{a_{33}}").move_to(self.equation)),
        )
        #3rd col
        self.play(Transform(pivot,SurroundingRectangle(self.A.get_rows()[2][2],color=YELLOW_E)),
                  Transform(b,SurroundingRectangle(self.B.get_rows()[2][0],color=YELLOW_E)),
                  Transform(ai,VGroup().add(SurroundingRectangle(self.A.get_rows()[2][0],color=BLUE_E),SurroundingRectangle(self.A.get_rows()[2][1],color=BLUE_E))),
                  Transform(xi,VGroup().add(SurroundingRectangle(self.X_0.get_columns()[0][0],color=BLUE_E),SurroundingRectangle(self.X_0.get_columns()[0][1],color=BLUE_E)))
                  )
        #write out new eq
        self.wait(1)
        self.play(Transform(self.equation,MathTex(r"x^{(1)}_3 = \frac{6 - 0- 0}{4}=\frac{3}{2}").move_to(self.equation)))
        # reveal result
        self.play(self.X_1.get_columns()[0][2].animate.set_color(WHITE))
        self.wait(1)
        self.play(VGroup().add(xi,ai,pivot,x,b).animate.set_opacity(0))
        #move on to next matrix
        self.play(self.AB.animate.shift(LEFT))
        self.X2.next_to(self.X1,LEFT)
        self.X_2.get_columns().set_color(BLACK)
        self.play(Write(self.X2))
        self.wait(2)
        # self.play(VGroup().add(xi,ai,pivot,x,b).animate.set_opacity(1))
        
        for j in range(3):
            if j==0:
                k=1
                l=2
            elif j==1:
                k=0
                l=2
            else:
                k=0
                l=1
            self.play(Transform(x,SurroundingRectangle(self.X_2.get_columns()[0][j],color=PURPLE)),
                    Transform(self.equation,MathTex(r"x^{(2)}_",j+1,r" = \frac{b_"+str(j+1)+r" - a_{"+str(j+1)+str(k+1)+"}x_{"+str(k+1)+"}^{(1)} - a_{"+str(j+1)+str(l+1)+"}x_{"+str(l+1)+"}^{(1)}}{a_{",j+1,j+1,r"}}").align_on_border(DOWN)),
            )
            #3rd col
            self.play(Transform(pivot,SurroundingRectangle(self.A.get_rows()[j][j],color=YELLOW_E)),
                    Transform(b,SurroundingRectangle(self.B.get_rows()[j][0],color=YELLOW_E)),
                    Transform(ai,VGroup().add(SurroundingRectangle(self.A.get_rows()[j][k],color=BLUE_E),SurroundingRectangle(self.A.get_rows()[j][l],color=BLUE_E))),
                    Transform(xi,VGroup().add(SurroundingRectangle(self.X_1.get_columns()[0][k],color=BLUE_E),SurroundingRectangle(self.X_1.get_columns()[0][l],color=BLUE_E)))
                    )
            #write out new eq
            self.wait(1)
            self.play(Transform(self.equation,MathTex(r"x^{(2)}_",j+1,r" = \frac{6 - \frac{3}{2}- \frac{3}{2}}{4}=\frac{3}{4}").align_on_border(DOWN)))
            # reveal result
            self.play(self.X_2.get_columns()[0][j].animate.set_color(WHITE))
            self.wait(1)
        self.play(VGroup().add(xi,ai,pivot,x,b).animate.set_opacity(0))
        #move on to next matrix
        self.play(self.AB.animate.shift(LEFT))
        self.X3.next_to(self.X2,LEFT)
        self.X_3.get_columns().set_color(BLACK)
        self.play(Write(self.X3))
        self.wait(2)
        for j in range(3):
            if j==0:
                k=1
                l=2
            elif j==1:
                k=0
                l=2
            else:
                k=0
                l=1
            self.play(Transform(x,SurroundingRectangle(self.X_3.get_columns()[0][j],color=PURPLE)),
                    Transform(self.equation,MathTex(r"x^{(3)}_",j+1,r" = \frac{b_"+str(j+1)+r" - a_{"+str(j+1)+str(k+1)+"}x_{"+str(j+1)+"}^{(2)} - a_{"+str(j+1)+str(l+1)+"}x_{"+str(j+1)+"}^{(2)}}{a_{",j+1,j+1,r"}}").align_on_border(DOWN)),
            )
            #3rd col
            self.play(Transform(pivot,SurroundingRectangle(self.A.get_rows()[j][j],color=YELLOW_E)),
                    Transform(b,SurroundingRectangle(self.B.get_rows()[j][0],color=YELLOW_E)),
                    Transform(ai,VGroup().add(SurroundingRectangle(self.A.get_rows()[j][k],color=BLUE_E),SurroundingRectangle(self.A.get_rows()[j][l],color=BLUE_E))),
                    Transform(xi,VGroup().add(SurroundingRectangle(self.X_2.get_columns()[0][k],color=BLUE_E),SurroundingRectangle(self.X_2.get_columns()[0][l],color=BLUE_E)))
                    )
            #write out new eq
            self.wait(1)
            self.play(Transform(self.equation,MathTex(r"x^{(3)}_",j+1,r" = \frac{6 - \frac{3}{4}- \frac{3}{4}}{4}=\frac{9}{8}").align_on_border(DOWN)))
            # reveal result
            self.play(self.X_3.get_columns()[0][j].animate.set_color(WHITE))
            self.wait(1)
        self.play(VGroup().add(xi,ai,pivot,x,b).animate.set_opacity(0))
        #move on to next matrix
        self.play(VGroup().add(self.X0,self.X1,self.X2,self.X3).animate.shift(RIGHT))
        self.X4.next_to(self.X3,LEFT)
        self.X_4.get_columns().set_color(BLACK)
        self.play(Write(self.X4))
        self.wait(2)
        for j in range(3):
            if j==0:
                k=1
                l=2
            elif j==1:
                k=0
                l=2
            else:
                k=0
                l=1
            self.play(Transform(x,SurroundingRectangle(self.X_4.get_columns()[0][j],color=PURPLE)),
                    Transform(self.equation,MathTex(r"x^{(4)}_",j+1,r" = \frac{b_"+str(j+1)+r" - a_{"+str(j+1)+str(k+1)+"}x_{"+str(k+1)+"}^{(3)} - a_{"+str(j+1)+str(l+1)+"}x_{"+str(l+1)+"}^{(3)}}{a_{",j+1,j+1,r"}}").align_on_border(DOWN)),
            )
            #3rd col
            self.play(Transform(pivot,SurroundingRectangle(self.A.get_rows()[j][j],color=YELLOW_E)),
                    Transform(b,SurroundingRectangle(self.B.get_rows()[j][0],color=YELLOW_E)),
                    Transform(ai,VGroup().add(SurroundingRectangle(self.A.get_rows()[j][k],color=BLUE_E),SurroundingRectangle(self.A.get_rows()[j][l],color=BLUE_E))),
                    Transform(xi,VGroup().add(SurroundingRectangle(self.X_3.get_columns()[0][k],color=BLUE_E),SurroundingRectangle(self.X_3.get_columns()[0][l],color=BLUE_E)))
                    )
            #write out new eq
            self.wait(1)
            self.play(Transform(self.equation,MathTex(r"x^{(4)}_",j+1,r" = \frac{6 - \frac{9}{8}- \frac{9}{8}}{4}=\frac{15}{16}").align_on_border(DOWN)))
            # reveal result
            self.play(self.X_4.get_columns()[0][j].animate.set_color(WHITE))
            self.wait(1)
        self.wait(3)
        
        self.play(VGroup().add(xi,ai,pivot,x,b).animate.set_opacity(0))
        #move on to next matrix
        self.play(VGroup().add(self.X0,self.X1,self.X2,self.X3,self.X4).animate.shift(RIGHT))
        self.X5.next_to(self.X4,LEFT)
        self.X_5.get_columns().set_color(BLACK)
        self.play(Write(self.X5))
        self.wait(2)
        for j in range(3):
            if j==0:
                k=1
                l=2
            elif j==1:
                k=0
                l=2
            else:
                k=0
                l=1
            self.play(Transform(x,SurroundingRectangle(self.X_5.get_columns()[0][j],color=PURPLE)),
                    Transform(self.equation,MathTex(r"x^{(5)}_",j+1,r" = \frac{b_"+str(j+1)+r" - a_{"+str(j+1)+str(k+1)+"}x_{"+str(k+1)+"}^{(4)} - a_{"+str(j+1)+str(l+1)+"}x_{"+str(l+1)+"}^{(4)}}{a_{",j+1,j+1,r"}}").align_on_border(DOWN)),
            )
            #3rd col
            self.play(Transform(pivot,SurroundingRectangle(self.A.get_rows()[j][j],color=YELLOW_E)),
                    Transform(b,SurroundingRectangle(self.B.get_rows()[j][0],color=YELLOW_E)),
                    Transform(ai,VGroup().add(SurroundingRectangle(self.A.get_rows()[j][k],color=BLUE_E),SurroundingRectangle(self.A.get_rows()[j][l],color=BLUE_E))),
                    Transform(xi,VGroup().add(SurroundingRectangle(self.X_4.get_columns()[0][k],color=BLUE_E),SurroundingRectangle(self.X_4.get_columns()[0][l],color=BLUE_E)))
                    )
            #write out new eq
            self.wait(1)
            self.play(Transform(self.equation,MathTex(r"x^{(5)}_",j+1,r" = \frac{6 - \frac{15}{16}- \frac{15}{16}}{4}=\frac{33}{32}").align_on_border(DOWN)))
            # reveal result
            self.play(self.X_5.get_columns()[0][j].animate.set_color(WHITE))
            self.wait(1)
        
        self.play(VGroup().add(xi,ai,pivot,x,b).animate.set_opacity(0))
        #move on to next matrix
        self.play(self.AB.animate.shift(1.5*LEFT))
        self.X6.next_to(self.X5,LEFT)
        self.X_6.get_columns().set_color(BLACK)
        self.play(Write(self.X6))
        self.wait(2)
        for j in range(3):
            if j==0:
                k=1
                l=2
            elif j==1:
                k=0
                l=2
            else:
                k=0
                l=1
            self.play(Transform(x,SurroundingRectangle(self.X_6.get_columns()[0][j],color=PURPLE)),
                    Transform(self.equation,MathTex(r"x^{(6)}_",j+1,r" = \frac{b_"+str(j+1)+r" - a_{"+str(j+1)+str(k+1)+"}x_{"+str(k+1)+"}^{(5)} - a_{"+str(j+1)+str(l+1)+"}x_{"+str(l+1)+"}^{(5)}}{a_{",j+1,j+1,r"}}").align_on_border(DOWN)),
            )
            #3rd col
            self.play(Transform(pivot,SurroundingRectangle(self.A.get_rows()[j][j],color=YELLOW_E)),
                    Transform(b,SurroundingRectangle(self.B.get_rows()[j][0],color=YELLOW_E)),
                    Transform(ai,VGroup().add(SurroundingRectangle(self.A.get_rows()[j][k],color=BLUE_E),SurroundingRectangle(self.A.get_rows()[j][l],color=BLUE_E))),
                    Transform(xi,VGroup().add(SurroundingRectangle(self.X_5.get_columns()[0][k],color=BLUE_E),SurroundingRectangle(self.X_5.get_columns()[0][l],color=BLUE_E)))
                    )
            #write out new eq
            self.wait(1)
            self.play(Transform(self.equation,MathTex(r"x^{(6)}_",j+1,r" = \frac{6 - \frac{33}{32}- \frac{33}{32}}{4}=\frac{63}{64}").align_on_border(DOWN)))
            # reveal result
            self.play(self.X_6.get_columns()[0][j].animate.set_color(WHITE))
            self.wait(1)
        self.wait(3)
        self.clear()
        self.play(Write(VGroup().add(Tex('Cette suite de vecteurs converge vers '),Matrix([[1],[1],[1]]),MathTex("X")).arrange(DOWN,0.5)) )
        self.wait(3)
        
    def subscene2(self):
        matR= Tex(r'L = ').next_to(A, 2*RIGHT)
        R= Matrix([["r_{11}",0,0],["r_{21}","r_{22}",0],["r_{31}","r_{32}","r_{33}"]],element_alignment_corner=[0, 0, 0.5],v_buff=1.3).next_to(matR,RIGHT)
        matRt= Tex(r'$L^\text{T}$ = ').next_to(R, 2*RIGHT)
        Rt= Matrix([["r_{11}","r_{21}","r_{31}"],[0,"r_{22}","r_{32}"],[0,0,"r_{33}"]],element_alignment_corner=[0, 0, 0.5],v_buff=1.3).next_to(matRt,RIGHT)
        self.play(Write(A))
        self.wait(4)
                
        