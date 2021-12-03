# "Responsibility of major emitters for country-level warming and extreme hot years" study code repository

## Citing this repository

This repository contains all the python code to reproduce the figures of the following paper:

Beusch, L., Nauels, A., Gudmundsson, L., Gütschow, J., Schleussner, C.-F., and Seneviratne, S. I.: Responsibility of major emitters for country-level warming and extreme hot years,  Commun. Earth Environ., in review, 2021.

If you use any code from this repository, please cite the associated paper.

## Using this repository

To run the scripts, follow their ordering:

- 1 trains MESMER (v0.8.2) for different ESMS and creates ESM-specific internal climate variability emulations.
- 2 preprocesses MAGICC (v6) output.
- 3 derives ESM-specific full emulations and grid-cell-level warming statistics.
- 4 derives grid-cell-level percentiles for the full ensemble of emulations for each of the warming statistics.
- 5 creates illustrative sample emulations.
- 6 carries out all the plotting and derives the numbers stated throughout the manuscript.

However, be aware that this code only works if all input data is saved in the same structures as we have stored it in and if you have all the required data available. Hence, it’s more likely that individual code snippets and checking out the general structure of our scripts are beneficial to you, rather than directly running the full code in this repository.

To reproduce the results shown in the study, the python packages mesmer v0.8.2 and regionmask v0.6.2 are required.

## Code versions

Revised paper submission release: v0.7.0

## License

Copyright (c) 2021 ETH Zurich, Lea Beusch.

The content of this repository is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 3 or (at your option) any later version.

The content of this repository is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with the content of this repository. If not, see https://www.gnu.org/licenses/.
