
from algo import*
from mainUI import*



def main():
    clock = pygame.time.Clock()
    names = ["Shuffle", "Quick Sort", "Bubble Sort", "Insertion Sort", "Heap Sort"]
    screen = pygame.display.set_mode((600,850))
    pygame.display.set_caption("Algorithms Visualization")
    chart = Chart(names)
    chart.shuffleChart()
    run = True
    while run:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = chart.click(pos)
                if clicked:
                    chart.select(clicked)
                    if clicked == 1:
                        chart.shuffleChart()
                    elif clicked == 2:
                        quickSort(chart.values,0,99,screen)
                    elif clicked == 3:
                        bubbleSort(chart.values,screen)
                    elif clicked == 4:
                        insertionSort(chart.values,screen)
                    elif clicked == 5:
                        heapSort(chart.values,screen)
         
        draw(screen,chart)

main()


