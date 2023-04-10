# Damped Pendulum
The motion of a damped pendulum can be studied by solving the following second order differential equation:
$$\LARGE\frac{d^2\theta}{dt^2}+{k}\frac{d\theta}{dt}+\frac{g}{l}sin\theta=0$$

where $\theta$ is the angular displacement of the pendulum from its equilibrium position, $t$ is time, $k$ is the damping coefficient, $g$ is the acceleration due to gravity, and $L$ is the length of the pendulum. 

This nonlinear equation can be solved by making a change of variable and introducing the angular velocity $\omega=\theta'(t)$. This results in a first-order system of differential equations:

$$\LARGE\theta'(t)=\frac{d\theta}{dt}=\omega(t)$$

$$\LARGE\omega'(t)=-k\omega-\frac{g}{l}sin\theta$$


</p>
<p align="center">
<img src="https://user-images.githubusercontent.com/53666707/112855420-0efbed80-90af-11eb-89c4-3224b01fc2b6.gif" width="550" height="600"/>
</p>
