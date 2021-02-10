# Elixir

Modeling blood flow and especially the propagation of the pulse wave in systemic
arteries is a topic that is interesting to the medical society since the shape of the
pressure profiles has diagnostic significance. We build a package that can
simulate blood flow and pressure in large arteries by solving a nonlinear onedimensional 
model based on the incompressible Navier-Stokes equations for a
Newtonian fluid in an elastic tube. Our method, however, does not require the
usage of discretized methods for solving differential equations such as the
popular Lax-Wendroff method (LW) but instead uses automatic differentiation to
achieve a similar result. 

Modeling blood flow and pressure in the systemic arteries has been a topic of
interest both to theoretical and clinical investigators. Thus, research in this area
has a vital interdisciplinary aspect. This project aims to develop a package capable
of performing such simulations using the models we develop to treat
cardiovascular diseases better. This is important since most deaths in developed
countries result from cardiovascular diseases, mostly associated with abnormal
flow in the arteries.

The original project's inspiration arose from previous and present efforts to
develop an anaesthesia simulator based on mathematical models. An important
part of which is having a good model for the cardiovascular system.
However, as stated previously, the traditional focus of such projects generally is
developing a good model.

The choice of the method to be used to solve the associated equations generally
comes from a standard list of such methods.

We present a new method that, unlike its predecessors, offers a continuous
solution, along with other benefits such as GPU support, a massive community,
and such like. 

Watch our video that highlights the fundamental idea of the project. 

[![Project Elixir - Team Disrupt](photo.png)](https://youtu.be/8Q4nvnozVsI "Project Elixir - Team Disrupt")
