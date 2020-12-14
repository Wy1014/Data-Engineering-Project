pipeline{
  agent any
  stages {
    stage('Build Flask app'){
      steps{
        sh 'docker build -i project .'
      }
    }
    stage('Run docker images'){
      parallel{
        stage('Run Redis'){
          steps{
            sh 'docker run -d -p 6379:6379 --name redis redis:alpine'
          }
        }
        stage('Run Flask App'){
          steps{
            sh 'docker run -d -p 5000:5000 --name project_c project'
          }
        }
      }
    }
    stage('Docker images down'){
      steps{
        sh 'docker rm -f redis'
        sh 'docker rm -f project_c'
        sh 'docker rmi -f project'
      }
    }
  }
}
