# Auto-Sum-of-Squares
自动配方机。

Automatically express a function in a sum-of-squares form.

<br>

# 环境 Environment:
1. Python3
2. Sympy包

<br>

# 使用说明 Tutorial
输入一个以x为单个自变量的有理函数，例（注：\**和^表示幂）：

输入自变量x的下界left，若留空则默认为0
输入函数的猜测极小值点，若留空则默认为0

程序将输出配方结果（极小值点选取不优、题目错误等问题可能导致尝试失败）

<br>

# 范例输入输出 Example Input and Output
  ## 输入：
  
  3/2*x^2+x/2+9/32-(x^3+14x\**2-3x)/(2x+4)
  
  0
  
  1.8
  
  ## 输出：
  通分化简后= ( 32*x\**\**3 - 112*x\**\**2 + 89*x + 18 )/(  32*x + 64 )
  
  上式分子= 
  
  32*x*(x - 9/5)\**\**2 +  ( 16*x\**\**2/5 - 367*x/25 + 18 )
  
  其中，二次函数部分 △ = b\*b-4*a*c =  -9311/625 <= 0
  
  因此函数 >=0 , 证毕
