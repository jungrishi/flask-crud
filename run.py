import os
import config
from flask import Flask

#import all the modules

def createApp():
  app=Flask(__name__)

  if os.environ.get('ENV') == 'production':
        app.config.from_object(config.ProductionConfig)
  else :
        app.config.from_object(config.DevelopmentConfig)



if __name__ =='__main__':
  app=createApp()
  print(app.config.get('PORT'))
  app.run(host=app.config.get('HOST'), port=app.config.get('PORT'))

