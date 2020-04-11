while True:
	try:
		x = int(input("Type a number: "))
		break
	except ValueError:
		print("\nThat\'s is not a valid number!")
	except KeyboardInterrupt:
		print("No input taken")
		break
	finally:
		print("\nAttempted input!\n")