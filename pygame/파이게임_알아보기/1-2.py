import sys, pygame

#pygame  모듈을 초기화하자
pygame.init()

#게임 창의 크기를 설정하자.
size = width, height = 320, 240

speed = [2, 2]
black = 0, 0, 0

#pygame은 이미지를 Surface 객체로 표현한다.
#pg.display.set_mode()는 new Surface를 만들며,
#실제 표시된 그래픽을 나타내는 새로운 Surface 객체를 생성합니다. 이 표면에 그리는 모든 그림은 모니터에 표시됩니다.
#그래픽 창을 만들자.
screen = pygame.display.set_mode(size) 

# load()는 ball data의 Surface 객체를 return한다.
ball = pygame.image.load("image.png")
ball = pygame.transform.scale(ball, (10, 10))
#파이게임에는 직사각형 영역을 나타내는 Rect라는 편리한 유틸리티 객체 유형이 제공됩니다. 나중에 코드의 애니메이션 부분에서 Rect 객체가 무엇을 할 수 있는지 살펴보겠습니다.
ballrect = ball.get_rect()

# 사용자 입력을 확인하고 공을 이동한 다음 공을 그립니다
while True:
    for event in pygame.event.get():
        #QUIT 이벤트가 발생했는지 확인합니다. 
        if event.type == pygame.QUIT: sys.exit()

#공의 위치를 업데이트 하자!
	#ballect 변수를 현재 속도만큼 이동합니다.
    ballrect = ballrect.move(speed)
    #공이 화면 밖으로 이동한 경우 속도를 역전시킵니다.
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
	#검은색 RGB 색상으로 화면을 채워서 화면을 지웁니다.
    screen.fill(black)
    #Surface.blit() 공 이미지를 화면에 그립니다
    #블릿은 기본적으로 한 이미지에서 다른 이미지로 픽셀 색상을 복사하는 것을 의미합니다. blit 메소드에 복사할 소스 표면과 소스를 대상에 배치할 위치를 전달합니다
    screen.blit(ball, ballrect)
    #디스플레이를 실제로 업데이트.
    #이렇게 하면 화면 Surface에 그린 모든 것이 표시됩니다.
    pygame.display.flip()