from skimage.feature import canny

#convert image to grayscale
coins = color.rgb2gray(coins)

#Apply image to grayscale
cooins = color.rgb2gray(coins)

#apply canny detector
canny_edges = canny(coins)

#show resulted image with edges
show_image(canny_edges, "Edges with canny")

#Apply canny detector with sigma of 0.5
canny_edges_0_5 = canny(coins, sigma=0.5)

#show resulted images with edges
show_image(canny_edges, "Sigma of 1")
show_image(canny_edges_0_5, "Sigma of 0.5")

