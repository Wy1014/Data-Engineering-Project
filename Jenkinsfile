pipeline{
  agent any
  stages {
    stage('Build Flask app'){
      steps{
        script{
          if(env.BRANCH_NAME == 'feature'){
            sh 'docker build -t project .'
          }
        }      
      }
    }
    stage('Run docker images'){
      parallel{
        stage('Run Flask App'){
          steps{
            script{
              if(env.BRANCH_NAME == 'feature'){
                sh 'docker run -d -p 5000:5000 --name project_c project'
              }  
            }
          }
        }
      }
    }
    stage('Testing'){
      steps{
        script{
          if(env.BRANCH_NAME == 'feature'){
            sh 'python unit_test.py'
          }
        }
      }
    }
    stage('Docker images down'){
      steps{
        script{
          if(env.BRANCH_NAME == 'feature'){
            sh 'docker rm -f project_c'
            sh 'docker rmi -f project'
          }
        }
      }
    }
  }  
}
