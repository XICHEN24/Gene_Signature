FROM knowengdev/base_image:11_09_2016 
MAINTAINER Xi Chen<xichen24@illinois.edu>

ENV SRC_LOC /home

# Install the latest knpackage
RUN pip3 install -I knpackage redis

# Clone from github
RUN git clone https://github.com/KnowEnG/Gene_Signature.git ${SRC_LOC} 

# Set up working directory
WORKDIR ${SRC_LOC}
 
