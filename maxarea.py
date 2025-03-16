def getMaxArea(w, h, isVertical, distance):
    vertical_cuts = {0, w}
    horizontal_cuts = {0, h}
    max_areas = []
   
    for i in range(len(isVertical)):
        if isVertical[i] == 1:
            vertical_cuts.add(distance[i])
        else:
            horizontal_cuts.add(distance[i])

        sorted_vertical = sorted(vertical_cuts)
        sorted_horizontal = sorted(horizontal_cuts)

        max_width = max(sorted_vertical[i+1] - sorted_vertical[i] for i in range(len(sorted_vertical) - 1))
        max_height = max(sorted_horizontal[i+1] - sorted_horizontal[i] for i in range(len(sorted_horizontal) - 1))

        max_areas.append(max_width * max_height)

    return max_areas