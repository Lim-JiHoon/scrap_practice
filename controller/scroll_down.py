import time
from module.chrome_instance import driver

class ScrollDown:
  def run(self): 
      isMouseScroll = False
      prev_height = self.getScrollHeight()
      
      # 반복 수행
      while True:       
          # 페이지 로딩 대기
          time.sleep(.1)
          
          self.executeScrollDown()
          # 현재 문서 높이를 가져와서 저장
          curr_height = self.getScrollHeight()        
          if curr_height == prev_height:            
              if time.time() - prevTime > 2:
                  break
          else:          
              prevTime = time.time()
              prev_height = curr_height

  def getScrollHeight(self):
      return driver.execute_script("return document.body.scrollHeight")

  def getScrollY(self):
      return driver.execute_script("return window.scrollY")

  def executeScrollDown(self):
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")