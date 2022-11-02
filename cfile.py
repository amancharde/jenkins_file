pipeline
{
  agent any
  stages
  {
    stage('build')
    {
      steps
      {
        i=4
        j=5
        k=i+j
        print("hello",k)
      }
    }
  }
}
