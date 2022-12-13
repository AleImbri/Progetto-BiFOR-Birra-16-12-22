import streamlit as st
from pag_spine import main as pag_spine
# from pag_burger import main as pag_burger
from pag_fritti import main as pag_fritti
# from pag_cocktail import main as pag_cocktail
from pag_bar import main as pag_bar


def main():
	
	################ load logo from web #########################
	from PIL import Image
	import requests
	from io import BytesIO
	url='https://frenzy86.s3.eu-west-2.amazonaws.com/fav/bdl.png'
	response = requests.get(url)
	image = Image.open(BytesIO(response.content))
	st.title("FAV BIG DATALAB PW BiFor")
	st.image(image, caption='',use_column_width=True)

				
	pag_name = ["Spine","Burger","Fritti","Cocktail","Bar"]
	
	OPTIONS = pag_name
	sim_selection = st.selectbox('Seleziona la pagina', OPTIONS)

	if sim_selection == pag_name[0]:
		pag_spine()
	elif sim_selection == pag_name[1]:
		pag_burger()
	elif sim_selection == pag_name[2]:
		pag_fritti()
	elif sim_selection == pag_name[3]:
		pag_cocktail()
	elif sim_selection == pag_name[4]:
		pag_bar()
	else:
		st.markdown("Something went wrong. We are looking into it.")


if __name__ == '__main__':
	main()