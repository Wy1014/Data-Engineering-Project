pipeline{
  agent any
  stages {
    stage('Build Flask app'){
      steps{
        script{
          if(env.BRANCH_NAME == 'develop' || env.BRANCH_NAME == 'release'){
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
              if(env.BRANCH_NAME == 'develop' || env.BRANCH_NAME == 'release'){
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
          if(env.BRANCH_NAME == 'develop'){
            sh 'python stress_test.py'
          }
          else if(env.BRANCH_NAME == 'release'){
            echo 'release-specific test'
          }
        }
      }
    }
    stage('Docker images down'){
      steps{
        script{
          if(env.BRANCH_NAME == 'develop'){
            sh 'docker rm -f project_c'
            sh 'docker rmi -f project'
          }
        }  
      }
    stage('Creating release branch'){
      steps{
        if(env.BRANCH_NAME == 'develop'){
          echo 'branch into release'
        }  
      }
    }
  }
}
