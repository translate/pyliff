<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="1.0"
    xmlns="urn:oasis:names:tc:xliff:document:2.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <xliff xmlns="urn:oasis:names:tc:xliff:document:2.0">
      <xsl:call-template name="files" />
    </xliff>
  </xsl:template>

  <xsl:template name="files">
    <xsl:for-each select="/*[local-name() = 'xliff']/*[local-name() = 'file']">
      <file>
	<xsl:call-template name="units" />
      </file>
    </xsl:for-each>
  </xsl:template>

  <xsl:template name="units">
    <xsl:for-each select="*[local-name() = 'body']/*[local-name() = 'trans-unit']">
      <unit>
	<xsl:call-template name="source" />
	<xsl:call-template name="target" />
      </unit>
    </xsl:for-each>
  </xsl:template>

  <xsl:template name="source">
    <xsl:for-each select="*[local-name() = 'source']">
      <source>
	<xsl:apply-templates/>
      </source>
    </xsl:for-each>
  </xsl:template>

  <xsl:template name="target">
    <xsl:for-each select="*[local-name() = 'target']">
      <target>
	<xsl:apply-templates/>
      </target>
    </xsl:for-each>
  </xsl:template>
</xsl:stylesheet>