
SIOT  = "Taller didáctico IOT.docx"

IOT:
	pandoc --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		--reference-doc=plantilla_IOT.docx \
		-o  $(SIOT)  \
		Cabecera.md  \
		Cabecera_latex.md \
		0.taller.md \
		1.microbit.md \
		2.componentes.md \
		3.Montaje_practico_Termometro.md \
		4.Montaje_practico_Termostaro.md \
		5.Programa_IOT.md \
		6.Raspberrypi.md \
		7.IOT.md \
		8.Preguntas_frecuentes.md

