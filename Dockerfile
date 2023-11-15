FROM konduit/jenkins-agent:miniconda-python3
USER jenkins
WORKDIR /home/jenkins
CMD ["cat"]
