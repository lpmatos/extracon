{{/*
Return extracon excel number.
*/}}
{{- define "extracon.excel.number" -}}
{{- if .Values.deployment.excel.number -}}
  {{- .Values.deployment.excel.number -}}
{{- else -}}
  {{- required "We need Extracon excel number" .Values.deployment.excel.number -}}
{{- end -}}
{{- end -}}

{{/*
Return telegram token.
*/}}
{{- define "telegram.token" -}}
{{- if .Values.deployment.telegram.token -}}
  {{- .Values.deployment.telegram.token | b64enc | quote -}}
{{- else }}
  {{- required "We need Telegram Token" .Values.deployment.telegram.token -}}
{{- end -}}
{{- end -}}

{{/*
Define all deployment environment vars in the format key:value.
*/}}
{{- define "deployment.envs" -}}
{{- range $KEY, $VALUE := .Values.deployment.envs }}
- name: {{ $KEY }}
  value: {{ $VALUE | quote }}
{{- end -}}
{{- end -}}
