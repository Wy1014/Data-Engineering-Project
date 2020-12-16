pipeline{
  agent any
  stages {
    stage('Build Flask app'){
      steps{
        sh 'docker build -t project .'   
      }
    }
    stage('Run docker images'){
      parallel{
        stage('Run Flask App'){
          steps{
            sh 'docker-compose up'
          }
        }
      }
    }
    stage('Testing'){
      steps{
        sh 'python stress_test.py'
      }
    }
    stage('Docker images down'){
      steps{
        sh 'docker rm -f project_c'
        sh 'docker rmi -f project' 
      }
    }
  }  
}
