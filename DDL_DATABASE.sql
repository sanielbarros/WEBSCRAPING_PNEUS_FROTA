-- DROP SCHEMA logistica;

CREATE SCHEMA logistica AUTHORIZATION postgres;

-- DROP SEQUENCE logistica.frotasaas_controle_pneus_em_uso_id_seq;

CREATE SEQUENCE logistica.frotasaas_controle_pneus_em_uso_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE logistica.frotasaas_controle_pneus_por_veiculo_id_seq;

CREATE SEQUENCE logistica.frotasaas_controle_pneus_por_veiculo_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE logistica.frotasaas_pneus_controle_atualizacao_sulcos_id_seq;

CREATE SEQUENCE logistica.frotasaas_pneus_controle_atualizacao_sulcos_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE logistica.frotasaas_pneus_que_retornaram_da_recauchutadora_id_seq;

CREATE SEQUENCE logistica.frotasaas_pneus_que_retornaram_da_recauchutadora_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE logistica.frotasaas_pneus_sucateados_por_modelo_id_seq;

CREATE SEQUENCE logistica.frotasaas_pneus_sucateados_por_modelo_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE logistica.frotasaas_relacao_calibragem_id_seq;

CREATE SEQUENCE logistica.frotasaas_relacao_calibragem_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;-- logistica.frotasaas_controle_pneus_em_uso definition

-- Drop table

-- DROP TABLE logistica.frotasaas_controle_pneus_em_uso;

CREATE TABLE logistica.frotasaas_controle_pneus_em_uso (
	id serial4 NOT NULL,
	cd_empresa int4 NULL,
	cd_filial int4 NULL,
	cd_ccusto int4 NULL,
	cd_pneu varchar(255) NULL,
	cd_modelo int4 NULL,
	nr_vida int4 NULL,
	qt_sulco1 float8 NULL,
	qt_sulco2 float8 NULL,
	qt_sulco3 float8 NULL,
	vl_custo float8 NULL,
	qt_sulco4 float8 NULL,
	qt_sulco5 float8 NULL,
	situacao varchar(255) NULL,
	lugar varchar(255) NULL,
	bl_baixa int4 NULL,
	cd_veiculo varchar(255) NULL,
	nm_modelo varchar(255) NULL,
	dh_evento varchar(255) NULL,
	cd_posicao varchar(255) NULL,
	cd_destino int4 NULL,
	cd_evento int4 NULL,
	bl_saida int4 NULL,
	bl_recauch int4 NULL,
	bl_compra int4 NULL,
	bl_inst int4 NULL,
	bl_desinst int4 NULL,
	bl_trent int4 NULL,
	nm_filial varchar(255) NULL,
	cd_regiona int4 NULL,
	nm_empresa varchar(255) NULL,
	cd_dimensa int4 NULL,
	cd_desenho int4 NULL,
	cd_fornec int4 NULL,
	cd_vei_loc varchar(255) NULL,
	qt_hr_even float8 NULL,
	qt_km_even int4 NULL,
	km_tperco int4 NULL,
	hr_tperco float8 NULL,
	nm_regiona varchar(255) NULL,
	nm_desenho varchar(255) NULL,
	nm_ccusto varchar(255) NULL,
	placa varchar(255) NULL,
	nm_fornec varchar(255) NULL,
	nm_dimensa varchar(255) NULL,
	data_atualizacao date NULL,
	CONSTRAINT frotasaas_controle_pneus_em_uso_pkey PRIMARY KEY (id)
);


-- logistica.frotasaas_controle_pneus_por_veiculo definition

-- Drop table

-- DROP TABLE logistica.frotasaas_controle_pneus_por_veiculo;

CREATE TABLE logistica.frotasaas_controle_pneus_por_veiculo (
	id serial4 NOT NULL,
	cd_veiculo varchar(255) NULL,
	placa varchar(255) NULL,
	cd_posicao varchar(255) NULL,
	qt_hr_even float8 NULL,
	qt_km_even int4 NULL,
	cd_modveic int4 NULL,
	aa_fabric int4 NULL,
	aa_modelo int4 NULL,
	qt_hr_med float8 NULL,
	qt_km_med int4 NULL,
	bl_tracao int4 NULL,
	bl_medprop int4 NULL,
	cd_cavalo varchar(255) NULL,
	nm_modveic varchar(255) NULL,
	nr_vida int4 NULL,
	cd_modelo int4 NULL,
	dot varchar(255) NULL,
	tt_km_vida int4 NULL,
	tt_hr_vida float8 NULL,
	tt_km_pneu int4 NULL,
	km_na_vida int4 NULL,
	tt_hr_pneu float8 NULL,
	hr_na_vida float8 NULL,
	qt_sulco_i float8 NULL,
	km_im_pri int4 NULL,
	km_re_pri int4 NULL,
	hr_im_pri float8 NULL,
	hr_re_pri float8 NULL,
	km_im_seg int4 NULL,
	km_re_seg int4 NULL,
	hr_im_seg float8 NULL,
	hr_re_seg float8 NULL,
	km_im_ter int4 NULL,
	km_re_ter int4 NULL,
	hr_im_ter float8 NULL,
	hr_re_ter float8 NULL,
	km_im_qua int4 NULL,
	km_re_qua int4 NULL,
	hr_im_qua float8 NULL,
	hr_re_qua float8 NULL,
	km_im_qui int4 NULL,
	km_re_qui int4 NULL,
	hr_im_qui float8 NULL,
	hr_re_qui float8 NULL,
	km_im_sex int4 NULL,
	km_re_sex int4 NULL,
	hr_im_sex float8 NULL,
	hr_re_sex float8 NULL,
	km_im_set int4 NULL,
	km_re_set int4 NULL,
	hr_im_set float8 NULL,
	hr_re_set float8 NULL,
	qt_libras float8 NULL,
	qt_sulco1 float8 NULL,
	qt_sulco2 float8 NULL,
	qt_sulco3 float8 NULL,
	qt_sulco4 float8 NULL,
	qt_sulco5 float8 NULL,
	cd_filial int4 NULL,
	nm_filial varchar(255) NULL,
	cd_regiona int4 NULL,
	cd_empresa int4 NULL,
	qt_hr_med1 float8 NULL,
	qt_km_med1 int4 NULL,
	cd_pneu varchar(255) NULL,
	nm_modelo varchar(255) NULL,
	cd_fornec int4 NULL,
	cd_dimensa int4 NULL,
	qt_sulco_c float8 NULL,
	qt_km_perc int4 NULL,
	qt_hr_perc float8 NULL,
	sulco_refo float8 NULL,
	qt_km_rod int4 NULL,
	qt_hr_rod float8 NULL,
	km_vida int4 NULL,
	hr_vida float8 NULL,
	nm_empresa varchar(255) NULL,
	nm_dimensa varchar(255) NULL,
	nm_fornec varchar(255) NULL,
	nm_regiona varchar(255) NULL,
	data_atualizacao date NULL,
	CONSTRAINT frotasaas_controle_pneus_por_veiculo_pkey PRIMARY KEY (id)
);


-- logistica.frotasaas_pneus_controle_atualizacao_sulcos definition

-- Drop table

-- DROP TABLE logistica.frotasaas_pneus_controle_atualizacao_sulcos;

CREATE TABLE logistica.frotasaas_pneus_controle_atualizacao_sulcos (
	id serial4 NOT NULL,
	cd_empresa int4 NULL,
	nm_empresa varchar(255) NULL,
	cd_filial int4 NULL,
	nm_filial varchar(255) NULL,
	cd_pneu varchar(255) NULL,
	dh_medicao varchar(255) NULL,
	cd_veiculo varchar(255) NULL,
	placa varchar(255) NULL,
	cd_posicao varchar(255) NULL,
	dh_instala varchar(255) NULL,
	sulco1 float8 NULL,
	sulco2 float8 NULL,
	sulco3 float8 NULL,
	sulco4 float8 NULL,
	sulco5 float8 NULL,
	data_atualizacao date NULL,
	CONSTRAINT frotasaas_pneus_controle_atualizacao_sulcos_pkey PRIMARY KEY (id)
);


-- logistica.frotasaas_pneus_que_retornaram_da_recauchutadora definition

-- Drop table

-- DROP TABLE logistica.frotasaas_pneus_que_retornaram_da_recauchutadora;

CREATE TABLE logistica.frotasaas_pneus_que_retornaram_da_recauchutadora (
	id serial4 NOT NULL,
	cd_empresa int4 NULL,
	nm_empresa varchar(255) NULL,
	cd_filial int4 NULL,
	nm_filial varchar(255) NULL,
	cd_fornec int4 NULL,
	nm_fornec varchar(255) NULL,
	cd_pneu varchar(255) NULL,
	nm_modelo varchar(255) NULL,
	cd_regiona varchar(255) NULL,
	nm_regiona varchar(255) NULL,
	vl_cons float8 NULL,
	vl_reform float8 NULL,
	qt_cons int4 NULL,
	qt_ref int4 NULL,
	data_atualizacao date NULL,
	data_retorno_recauchutadora date NULL,
	CONSTRAINT frotasaas_pneus_que_retornaram_da_recauchutadora_pkey PRIMARY KEY (id)
);


-- logistica.frotasaas_pneus_sucateados_por_modelo definition

-- Drop table

-- DROP TABLE logistica.frotasaas_pneus_sucateados_por_modelo;

CREATE TABLE logistica.frotasaas_pneus_sucateados_por_modelo (
	id serial4 NOT NULL,
	qt_km_pri float8 NULL,
	qt_hr_pri float8 NULL,
	qt_km_seg float8 NULL,
	qt_hr_seg float8 NULL,
	qt_km_ter float8 NULL,
	qt_hr_ter float8 NULL,
	qt_km_qua float8 NULL,
	qt_hr_qua float8 NULL,
	qt_km_qui float8 NULL,
	qt_hr_qui float8 NULL,
	qt_km_sex float8 NULL,
	qt_hr_sex float8 NULL,
	qt_km_set float8 NULL,
	qt_hr_set float8 NULL,
	nm_desenho varchar(255) NULL,
	cd_pneu varchar(255) NULL,
	nm_fornec varchar(255) NULL,
	dh_evento varchar(255) NULL,
	cd_modelo int4 NULL,
	vl_custo float8 NULL,
	nm_fabrica varchar(255) NULL,
	nm_motsuca varchar(255) NULL,
	nm_dimensa varchar(255) NULL,
	nm_filial varchar(255) NULL,
	nm_empresa varchar(255) NULL,
	cd_filial int4 NULL,
	cd_empresa int4 NULL,
	cd_veiculo varchar(255) NULL,
	data_atualizacao date NULL,
	CONSTRAINT frotasaas_pneus_sucateados_por_modelo_pkey PRIMARY KEY (id)
);


-- logistica.frotasaas_relacao_calibragem definition

-- Drop table

-- DROP TABLE logistica.frotasaas_relacao_calibragem;

CREATE TABLE logistica.frotasaas_relacao_calibragem (
	id serial4 NOT NULL,
	cd_empresa int4 NULL,
	cd_pneu varchar(255) NULL,
	dh_evento varchar(255) NULL,
	cd_posicao varchar(255) NULL,
	qt_km int4 NULL,
	cd_motdesi varchar(255) NULL,
	cd_tprecau varchar(255) NULL,
	cd_desenho varchar(255) NULL,
	libras float8 NULL,
	libras_ini float8 NULL,
	cd_evento int4 NULL,
	qt_hr float8 NULL,
	cd_tpborra varchar(255) NULL,
	cd_destino varchar(255) NULL,
	cd_motsuca varchar(255) NULL,
	nm_modelo varchar(255) NULL,
	nr_vida int4 NULL,
	cd_filial int4 NULL,
	cd_veiculo varchar(255) NULL,
	placa varchar(255) NULL,
	nm_fabrica varchar(255) NULL,
	nm_dimensa varchar(255) NULL,
	nm_empresa varchar(255) NULL,
	nm_filial varchar(255) NULL,
	nm_modveic varchar(255) NULL,
	data_atualizacao date NULL,
	CONSTRAINT frotasaas_relacao_calibragem_pkey PRIMARY KEY (id)
);