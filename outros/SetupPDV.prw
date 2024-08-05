#INCLUDE "Protheus.ch"
#include "TOPCONN.CH"
#Include "TbiConn.ch"
#Include "APWEBEX.CH"

Static cOpcSelect

User Function SetupPDV()

	Local lNext

	cOpcSelect := ""

	lNext := TelaHome(1)

	If lNext
		If lNext .And. "01" $ cOpcSelect
			lNext := TelaHome(2)
		EndIf
		If lNext .And. "02" $ cOpcSelect
			lNext := TelaHome(3)
		EndIf
		If lNext .And. "03" $ cOpcSelect
			lNext := TelaHome(4)
		EndIf
	EndIf

Return()

Static Function TelaHome(nOpc)

	Local oFont1 := TFont():New("MS Sans Serif",,020,,.T.,,,,,.F.,.F.)
	Local oGroup1
	Local oSay1
	Local oSay2
	Local oSay3
	Local oSay4
	Local oSay5
	Local oSay6
	Local oSay7
	Local oSay8
	Local oSay9
	Local oSay10
	Local oSButton1
	Local oSButton2
	//Local oSButton3
	Local cTextoTela := ""
	Local oGet1
	Local oGet2
	Local oGet3
	Local oGet4
	Local oGet5
	Local oGet6
	Local oGet7
	Local oGet8
	Local oRadMenu1 
	Private cGet1   :=	Space(6)  // 999.999.999.999 IP 
	Private cGet2
	Private cGet3	:=	Space(15) // 999.999.999.999 IP
	Private cGet4 
	Private cGet5
	Private cGet6
	Private cGet7
	Private cGet8
	Private nRadMenu1
	Private lRet := .F.
	Private oWBrowse1
	Private aWBrowse1 := {}
	Private oOk := LoadBitmap( GetResources(), "LBOK" )
	Private oNo := LoadBitmap( GetResources(), "LBNO" )
	Private nTcConn
	Private cCodFil := FWCodFil() //Filial logado
	Private cEmp    := FWCodEmp()
	Private oServer := Nil // Objeto que chama Classe de RPC
	Private lConect := .T. // Reotrno de RPC fez comunicação
	Static oDlg

	DbSelectArea("MDG")
	MDG->(DbGoTop())
	MDG->(DbSetOrder(1))

	If nOpc == 1
	
		cTextoTela := "CONFIGURACAO DA FILIAL " + cCodFil
	
	ElseIf nOpc == 2
	
		cTextoTela := "PREENCHA OS PARAMETROS DE CONFIGURACAO DO PDV"
		cGet1 := SuperGetMv('MV_LJAMBIE',,' ')
		cGet2 := SuperGetMv('MV_NFCEURL',,' ')
		cGet3 := "10.61.0.32          "
		cGet4 := "140"+cCodFil+"     "
		cGet5 := "ENVIRONMENT    "
		cGet6 := Space(3)
		cGet7 := MDG->MDG_IPSIT
		cGet8 := SuperGetMv('PB_VGETORC',,' ')//"10.61.0.32:3013     "
		nRadMenu1 := 2
	
	EndIf

	DEFINE MSDIALOG oDlg TITLE "Setup PDV" FROM 000, 000  TO 400, 600 COLORS 0, 16777215 PIXEL
	
	@ 004, 005 SAY oSay1 PROMPT cTextoTela SIZE 290, 011 OF oDlg FONT oFont1 COLORS 0, 16777215 PIXEL
	@ 018, 005 GROUP oGroup1 TO 176, 295 PROMPT "Setup" OF oDlg COLOR 0, 16777215 PIXEL
	
	If nOpc == 1
	
		@ 027, 010 LISTBOX oWBrowse1 Fields HEADER "  ","Descricao" SIZE 280, 143 OF oDlg PIXEL ColSizes 50,50
		oWBrowse1:bLDblClick := {|| aWBrowse1[oWBrowse1:nAt,1] := !aWBrowse1[oWBrowse1:nAt,1],oWBrowse1:DrawSelect()}
	
		ListaParm(nOpc)
	
	ElseIf nOpc == 2

		cGet1 := PadR(Alltrim(GetMV("MV_LJAMBIE")),6,"") //Tamanho do IP 
		cGet2 := GetMV("MV_NFCEURL")
		cGet2 := GetMV("MV_SPEDURL")
		cGet3 := PadR(Alltrim(GetMV("MV_LJILLIP")),15,"") //Tamanho do IP
		cGet4 := GetMV("MV_LJILLPO")
		cGet5 := GetMV("MV_LJILLEN")
		cGet8 := GetMv('PB_VGETORC')

		@ 030, 015 SAY oSay2 PROMPT "Ambiente:" SIZE 027, 007 OF oDlg COLORS 0, 16777215 PIXEL
		@ 028, 045 MSGET oGet1 VAR cGet1 SIZE 031, 010 OF oDlg COLORS 0, 16777215 PIXEL
		@ 050, 015 SAY oSay3 PROMPT "URL TSS:" SIZE 029, 007 OF oDlg COLORS 0, 16777215 PIXEL
		@ 048, 045 MSGET oGet2 VAR cGet2 SIZE 170, 010 OF oDlg COLORS 0, 16777215 PIXEL
		@ 070, 015 SAY oSay4 PROMPT "IP para carga de dados:" SIZE 062, 007 OF oDlg COLORS 0, 16777215 PIXEL
		@ 068, 075 MSGET oGet3 VAR cGet3 SIZE 140, 010 OF oDlg COLORS 0, 16777215 PIXEL
		@ 090, 015 SAY oSay6 PROMPT "Porta para carga de dados:" SIZE 068, 007 OF oDlg COLORS 0, 16777215 PIXEL
		@ 088, 083 MSGET oGet4 VAR cGet4 SIZE 080, 010 OF oDlg COLORS 0, 16777215 PIXEL
		@ 110, 015 SAY oSay7 PROMPT "Ambiente para carga de dados:" SIZE 079, 007 OF oDlg COLORS 0, 16777215 PIXEL
		@ 108, 093 MSGET oGet5 VAR cGet5 SIZE 072, 010 OF oDlg COLORS 0, 16777215 PIXEL
		@ 130, 015 SAY oSay8 PROMPT "Código da Estaãao:" SIZE 052, 007 OF oDlg COLORS 0, 16777215 PIXEL
		@ 128, 064 MSGET oGet6 VAR cGet6 SIZE 029, 010 OF oDlg COLORS 0, 16777215 PIXEL
		@ 130, 130 SAY oSay5 PROMPT "Habilita PAF-ECF?" SIZE 050, 007 OF oDlg COLORS 0, 16777215 PIXEL
		@ 126, 180 RADIO oRadMenu1 VAR nRadMenu1 ITEMS "SIM","NAO" SIZE 028, 019 OF oDlg COLOR 0, 16777215 PIXEL
		@ 150, 015 SAY oSay9 PROMPT "IP SITEF:" SIZE 027, 007 OF oDlg COLORS 0, 16777215 PIXEL
		@ 148, 043 MSGET oGet7 VAR cGet7 SIZE 078, 010 OF oDlg COLORS 0, 16777215 PIXEL
		@ 150, 130 SAY oSay10 PROMPT "IP Web Service:" SIZE 045, 007 OF oDlg COLORS 0, 16777215 PIXEL
		@ 148, 172 MSGET oGet8 VAR cGet8 SIZE 090, 010 OF oDlg COLORS 0, 16777215 PIXEL
	
	ElseIf nOpc == 3 .Or. nOpc == 4
	
		@ 027, 010 LISTBOX oWBrowse1 Fields HEADER "  ","Tabela","Descricao" SIZE 280, 143 OF oDlg PIXEL ColSizes 50,50
		oWBrowse1:bLDblClick := {|| aWBrowse1[oWBrowse1:nAt,1] := !aWBrowse1[oWBrowse1:nAt,1],oWBrowse1:DrawSelect()}
		oWBrowse1:bHeaderClick := {|oList, nCol| sfMarkLis (oList, nCol)   }
		ListaParm(nOpc)
	
	EndIf
	//    DEFINE SBUTTON oSButton3 FROM 182, 190 TYPE 20 OF oDlg ENABLE
	DEFINE SBUTTON oSButton2 FROM 182, 227 TYPE 19 OF oDlg ENABLE ACTION NextTela(nOpc)
	DEFINE SBUTTON oSButton1 FROM 182, 265 TYPE 02 OF oDlg ENABLE ACTION oDlg:End()

	ACTIVATE MSDIALOG oDlg CENTERED

Return lRet
//------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------
/*/{Protheus.doc} sfMarkLis
Marca e desmarca a Lista com base na Primeria Coluna
@type function
@version  12.1.33 cTree
@author Handerson L.Duarte
@since 22/02/2022
@param mvObjLis, Object, Objeto LISTBOX
@param mvColun, Numeric, Numero da Coluna selecinada pelo usuário.
/*/
//------------------------------------------------------------------------------------
Static Function sfMarkLis (mvObjLis as Object, mvColun as Numeric)
    Local niCont:=1
    If mvColun==1 //Somente A Primeira Coluna
        For niCont:=1 to Len ( mvObjLis:Aarray)
            mvObjLis:Aarray[niCont,mvColun] := ! mvObjLis:Aarray[niCont,mvColun]
            mvObjLis:DrawSelect()
        Next niCont
        mvObjLis:Refresh()
    EndIf
Return ()
//------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------


Static Function ListaParm(nOpc)

	Local oServer   := Nil // Objeto que chama Classe de RPC
	Local lConect   := .T. // Reotrno de RPC fez comunicação
	Local cIp 	:= Alltrim(GetMV("MV_LJILLIP"))
	Local nPort	:= val(GetMV("MV_LJILLPO"))
	Local cAmb 	:= Alltrim(GetMV("MV_LJILLEN"))
	
	aWBrowse1 := {}

	If nOpc == 1
	
		Aadd(aWBrowse1,{.F.,"01 - Parametrizaãao"})
		Aadd(aWBrowse1,{.F.,"02 - Carga de Tabelas"})
		Aadd(aWBrowse1,{.F.,"03 - Carga de Preço"})

		oWBrowse1:SetArray(aWBrowse1)
		oWBrowse1:bLine := {|| { If( aWBrowse1[oWBrowse1:nAt,1],oOk,oNo),aWBrowse1[oWBrowse1:nAt,2] } }

	ElseIf nOpc == 3 .Or. nOpc == 4
	
		// Ip e porta do Server que o RPC se conectara
		oServer := FwRpc():New(cIp,nPort,cAmb)        
		
		oServer:SetRetryConnect(1)   
		
		lConect := oServer:Connect()                          
		
		//Conout(VarInfo("lConect ListaParm",lConect,,.F.,.F.))
		
		//Prepara Ambiente
		oServer:SetEnv(cEmp, cCodFil, "PDV")        
		
		// Inicia repeticoes
		If lConect
			aWBrowse1 := oServer:CallProc("U_TabRet", nOpc)
		Else	
			alert("Erro ao tentar conectar na retaguarda, por favor verifique os parametros de conexao")
			oServer:Disconnect()
			Return()
		EndIf
		
		//Desconecta do servidor
		oServer:Disconnect()

		If Len(aWBrowse1) > 0
		
			oWBrowse1:SetArray(aWBrowse1)
		
			oWBrowse1:bLine := {|| { If( aWBrowse1[oWBrowse1:nAt,1],oOk,oNo),aWBrowse1[oWBrowse1:nAt,2],aWBrowse1[oWBrowse1:nAt,3],aWBrowse1[oWBrowse1:nAt,4],aWBrowse1[oWBrowse1:nAt,5] } }
		
		EndIf

	EndIf

Return()



Static Function NextTela(nOpc)

	Local nI

	If nOpc == 1
		lRet := .T.
		For nI := 1 To Len(aWBrowse1)
			If aWBrowse1[nI,1]
				cOpcSelect += Left(aWBrowse1[nI,2],2) + "/"
			EndIf
		Next nI

	ElseIf nOpc == 2

		lRet := .T.
		PutMV("MV_LJAMBIE",AllTrim(cGet1))
		PutMV("MV_NFCEURL",AllTrim(cGet2))
		PutMV("MV_SPEDURL",AllTrim(cGet2))
		PutMV("MV_LJILLIP",AllTrim(cGet3))
		PutMV("MV_LJILLPO",cGet4)
		PutMV("MV_LJILLEN",AllTrim(cGet5))
		PutMV("MV_LJILLCO",Substr(cCodFil,1,2))
		PutMV("MV_LJILLBR",cCodFil)
		PutMV("MV_ESTADO" ,SM0->M0_ESTCOB)	
		PutMV("MV_EMPTEF" ,PadL(cCodFil,8,"0"))
		PutMV("MV_CXLOJA" ,"A"+cCodFil+"/00001/0000000001")	
		PutMV("MV_LJPAFEC",If(nRadMenu1 == 1,.T.,.F.))
		PutMV("MV_CLIPAD" ,"000P"+cCodFil)
		PutMV("MV_LOJAPAD","01")

	ElseIf nOpc == 3 .Or. nOpc == 4

		FWMsgRun(, {|oSay| ImportTabs( oSay ) }, "Importação de Dados", "Iniciando importação..." )	

		lRet := .T.	

	EndIf

	oDlg:End()

Return

/*
*Funcao: ImprtTables()
*Descr: Importa??o da tabela da retaguarda para pdv local
*Autor: Maed Gaudencio Ramos
*Data: 16/12/2019
*/

Static Function ImportTabs(oSay)

	Local aDados    	:= {}
	Local nI        	:= 0
	Local cIp 			:= Alltrim(GetMV("MV_LJILLIP"))
	Local nPort			:= val(GetMV("MV_LJILLPO"))
	Local cAmb 			:= Alltrim(GetMV("MV_LJILLEN"))
	Local nTotal        := 0
	Local xY            := 0
	Local xI			:= 0
	Private aCampos   	:= {}
	Private cTabela   	:= " "
	Private aSetField 	:= {}

	For nI := 1 To Len(aWBrowse1)

		If aWBrowse1[nI,1]

			// Ip e porta do Server que o RPC se conectara
			oServer := FwRpc():New(cIp,nPort,cAmb)               
			oServer:SetRetryConnect(1)   
			
			lConect := oServer:Connect()                          
			
			//Conout(VarInfo("lConect ImportTabs",lConect,,.F.,.F.))
			
			//Prepara Ambiente
			oServer:SetEnv(cEmp, cCodFil, "PDV")        
			
			// Inicia repeticoes
			If lConect
				aDados := oServer:CallProc("U_ImpTab",AllTrim(aWBrowse1[nI,2])/*cTabela*/,AllTrim(aWBrowse1[nI,4])/*cFiltro*/,AllTrim(aWBrowse1[nI,5])/*cSeek*/)
			Else	
				alert("Erro ao tentar conectar na retaguarda, por favor verifique os parametros de conexao")
				oServer:Disconnect()
				Return()
			EndIf
			
			//Desconecta do servidor
			oServer:Disconnect()

			//Realiza a gravacao dos dados na tabela
			If len(aDados) > 0
				
				DbSelectArea(AllTrim(aWBrowse1[nI,2]))

				//Limpar a tabela para nao duplicar os registro.
				If DelTab(AllTrim(aWBrowse1[nI,2]))
				
					If Len(aDados) > 0  

						nTotal := Len(aDados) 
				
						For xI := 1 To Len(aDados)

							//Conout(VarInfo("Total Registro: ",nTotal,,.F.,.F.))

							(AllTrim(aWBrowse1[nI,2]))->(DbAppend())
							
							For xY := 1 To len(aDados[xI]) //Pega os campos e dados
								
								If aDados[xI,xY,3]  == "C"
									(AllTrim(aWBrowse1[nI,2]))->&(aDados[xI,xY,1]) := aDados[xI,xY,2]
								ElseIf aDados[xI,xY,3]  == "N"
									(AllTrim(aWBrowse1[nI,2]))->&(aDados[xI,xY,1]) := aDados[xI,xY,2]
								ElseIf aDados[xI,xY,3]  == "D"
									(AllTrim(aWBrowse1[nI,2]))->&(aDados[xI,xY,1]) := Stod(aDados[xI,xY,2])
								ElseIf aDados[xI,xY,3]  == "L"
									(AllTrim(aWBrowse1[nI,2]))->&(aDados[xI,xY,1]) := If(aDados[xI,xY,2] == "T",.T.,.F.)
								ElseIf aDados[xI,xY,3]  == "M"
									(AllTrim(aWBrowse1[nI,2]))->&(aDados[xI,xY,1]) := aDados[xI,xY,2]
								Endif
														
							Next xY 

							(AllTrim(aWBrowse1[nI,2]))->(DbCommit())

							nTotal--

						Next xI
				
					EndIf

				EndIf
			
			EndIf
		
			oSay:cCaption := "Processando tabela " + AllTrim(aWBrowse1[nI,2]) + "! "
			ProcessMessages()
		
		EndIf

	Next nI

	MsgInfo("Importacao realizada")

Return()

/*
*Função: TabRet()
*Desc: Dados das tabelas para importacoes
*Autor: Maed Gaudencio Ramos
*Data: 13/12/2019
*/

User Function TabRet(xOpc)

	Local aWBrowse1 := {}
	Local nOpcao	:= xOpc

	cQuery := "SELECT "
	cQuery += "		ZX5_CHAVE  AS TABELA, " 
	cQuery += "		ZX5_DESC01 AS DESCRICAO, " 
	cQuery += "		ZX5_DESC02 AS FILTRO, "
	cQuery += "		TRIM(ZX5_DESC03)||TRIM(ZX5_DESC04) AS SEEK "
	cQuery += " FROM " + RetSqlName("ZX5") + "  
	cQuery += " WHERE "
	cQuery += "		ZX5_FILIAL = '"+xFilial("ZX5")+"' "
	If nOpcao == 3
		cQuery += "		AND ZX5_TABELA = 'PDV' "
	ElseIf nOpcao == 4
		cQuery += "		AND ZX5_TABELA = 'PRE' "
	EndIf		
	cQuery += "		AND D_E_L_E_T_ = ' ' "
	OPEN QUERY cQuery ALIAS "TMPZX5"
	
	While TMPZX5->(!EOF())
		AAdd( aWBrowse1, {.T.,TMPZX5->TABELA,TMPZX5->DESCRICAO,TMPZX5->FILTRO,TMPZX5->SEEK} )
		TMPZX5->(DbSkip())
	EndDo
	
	CLOSE QUERY "TMPZX5"
	
Return(aWBrowse1)

/*
*Função: ImpTab()
*Desc: Impotarcaoo das tabelas com a retaguarda de acordo com a ZX5 tabela PDV
*Autor: Maed Gaudencio Ramos
*Data: 13/12/2019
*/

User Function ImpTab(cTabela,cFiltro,cSeek)

	Local cCpoFilial
	Local nTotReg
	Local nCtd
	Local cQuery
	Local aCampos   := {}
	Local aSetField := {}
	Local aAuxDados := {}
	Local aImpDados := {}
	Local xConteudo := ""
	Local nI := 0
	
	DbSelectArea(cTabela)
	(cTabela)->(DbSetOrder(1))

	cAlias := "X"+cTabela	// Alias auxiliar para conexão remota

	cCpoFilial := If(Left(cAlias,2) == "XS",Right(cAlias,2),cTabela)+"_FILIAL"	// Nome do campo filial

	cQuery := "SELECT 
	cQuery += "		COUNT(*) AS QTDREG 
	cQuery += "FROM " 
	cQuery += " " + RetSqlName(cTabela) + " "  
	cQuery += "WHERE "+cCpoFilial+" = '"+xFilial(cTabela)+"' 
	cQuery += "AND D_E_L_E_T_ = ' ' " + If(Empty(cFiltro)," "," AND " + cFiltro) + " 
	OPEN QUERY cQuery ALIAS cAlias		

	(cAlias)->(DbGoTop())

	nTotReg := (cAlias)->QTDREG

	nCtd := 1

	CLOSE QUERY cAlias

	DO CASE

		Case cTabela = "SB1"

			cQuery := "SELECT "
			cQuery += " * "
			cQuery += "FROM " 
			cQuery += "	" + RetSqlName("SB1") + " "
			cQuery += "WHERE "
			cQuery += "B1_FILIAL = ' ' "
			cQuery += "AND B1_TIPO IN ('01','02') "
			cQuery += "AND B1_MSBLQL != '1' "
			cQuery += "AND D_E_L_E_T_ = ' ' "

		Case cTabela = "DA1"

			cQuery := "	SELECT "
			cQuery += "	DA1.* "
			cQuery += "	FROM "
			cQuery += "	" + RetSqlName("DA0") + " DA0,"
			cQuery += "	" + RetSqlName("DA1") + " DA1 "
			cQuery += "	WHERE "
			cQuery += "		DA1.DA1_CODTAB      = DA0.DA0_CODTAB "
			cQuery += "		AND DA1_FILIAL      = DA0.DA0_FILIAL "
			cQuery += "		AND DA1.D_E_L_E_T_  = DA0.D_E_L_E_T_ "
			cQuery += "		AND DA1.D_E_L_E_T_  = ' ' "
			cQuery += "		AND (DA0_DATATE >= '"+DTOS(dDataBase)+"'  OR DA0_DATATE = ' ') "
			cQuery += "		AND DA0.DA0_XTIPO   != '2' "
			cQuery += "		AND DA0.DA0_FILIAL  = '"+FWCodFil() +"'  "
			cQuery += "		AND DA1.DA1_ATIVO   = '1' "
			cQuery += "		AND DA0.D_E_L_E_T_ = ' ' "

		Case cTabela = 'DA0'

			cQuery := "SELECT "
			cQuery += "	* "
			cQuery += "FROM "
			cQuery += "	" + RetSqlName(cTabela) + " "
			cQuery += "WHERE "
			cQuery += "		(DA0_DATATE >= '"+DTOS(dDataBase)+"'  OR DA0_DATATE = ' ') "
			cQuery += "		AND DA0_XTIPO != '2' "
			cQuery += "		AND DA0_FILIAL = '"+FWCodFil() +"'  "
			cQuery += "		AND D_E_L_E_T_ = ' ' "

		Case cTabela = 'SX5'

			cQuery := "SELECT "
			cQuery += "	* "
			cQuery += "FROM "
			cQuery += "	" + RetSqlName(cTabela) + " "
			cQuery += "WHERE "
			cQuery += "		X5_FILIAL IN (' ','"+FWCodFil()+"') "
			cQuery += "		AND D_E_L_E_T_ = ' ' "

		OTHERWISE	

			cQuery := "SELECT * FROM " + RetSqlName(cTabela) + " WHERE "+cCpoFilial+" = '"+xFilial(cTabela)+"' AND D_E_L_E_T_ = ' '" + If(Empty(cFiltro)," "," AND " + cFiltro)

	END CASE

	OPEN QUERY cQuery ALIAS cAlias	

	AEval(FWSX3Util():GetAllFields(cTabela, .F.), {|Campo| Aadd(aCampos, {Campo, X3Obrigat(Campo)}), Aadd(aSetField, {Campo, GetSX3Cache(Campo, "X3_TIPO"), TamSX3(Campo)[1], TamSX3(Campo)[2]})})

	(cAlias)->(DbGoTop())

	While (cAlias)->(!EOF())

		aAuxDados := {}

		For nI := 1 To Len(aCampos)  // Adiciona campos ao array para o append
			
			nPos := (cAlias)->(FieldPos(aCampos[nI, 1]))
			
			If nPos > 0

				xConteudo := (cAlias)->(FieldGet(nPos))

				If !Empty(xConteudo)  // So grava campos com conteudo
				
					Aadd(aAuxDados, {aCampos[nI,1], xConteudo, aSetField[nI,2]})
					
				EndIf

			EndIf

		Next nI

		aAdd(aImpDados,aAuxDados)

		(cAlias)->(DbSkip())

		nCtd++

	EndDo

	CLOSE QUERY cAlias
		
Return(aImpDados)


/*
*Função: DelTab()
*Desc: Limpa os dados para não replicar os dados
*Autor: Maed Gaudencio Ramos
*Data: 17/01/2022
*/

Static Function DelTab(xTabela)

	Local cDelet 	:= " "
	Local cTabela 	:= xTabela
	Local nErro     := 0
	Local lRet      := .T.

	cDelet := " DELETE FROM " + RetSqlName(cTabela) + " "
	nErro := TcSqlExec(cDelet)

	If nErro != 0
		lRet := .F.
        MsgStop("Erro na exclusao da tabela: "+cTabela+": "+TcSqlError(), "Atenção")
    EndIf
	
   
Return(lRet)
