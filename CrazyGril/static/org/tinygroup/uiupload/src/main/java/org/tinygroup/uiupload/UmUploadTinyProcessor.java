package org.tinygroup.uiupload;

import java.io.IOException;

import javax.servlet.ServletException;

import org.tinygroup.commons.tools.StringUtil;
import org.tinygroup.vfs.FileObject;
import org.tinygroup.weblayer.AbstractTinyProcessor;
import org.tinygroup.weblayer.WebContext;
import org.tinygroup.weblayer.listener.ServletContextHolder;
import org.tinygroup.weblayer.listener.TinyServletContext;

/**
 * 图片上传
 * 
 * @author renhui
 *
 */
public class UmUploadTinyProcessor extends AbstractTinyProcessor {

	@Override
	protected void customInit() throws ServletException {

	}

	@Override
	public void reallyProcess(String urlString, WebContext context)
			throws ServletException, IOException {
		String type = context.get("t");
		StringBuffer buffer = new StringBuffer();
		if(type!=null&&type.equals("ckeditor")){
			FileObject fileObject = context.get("upload");
			TinyServletContext servletContext=(TinyServletContext) ServletContextHolder.getServletContext();
			String realPath = servletContext.getOriginalContext().getRealPath("/");
			buffer.append("<script type=\"text/javascript\">")
					.append("window.parent.CKEDITOR.tools.callFunction(")
					.append(context.get("CKEditorFuncNum"))
					.append(",window.parent.contextPath+'")
					.append(resolverFilePath(
							fileObject.getAbsolutePath(),
							realPath))
					.append("','')");
			buffer.append("</script>");

		}else if(type!=null&&type.equals("webupload")){
			FileObject fileObject = context.get("webfile");			
			TinyServletContext servletContext=(TinyServletContext) ServletContextHolder.getServletContext();
			String realPath = servletContext.getOriginalContext().getRealPath("/");
			buffer.append("{'url' : '")
					.append(resolverFilePath(
							fileObject.getAbsolutePath(),
							realPath))
					.append("', 'result' : 'success', 'id' : 'id'}");
		}else{
			FileObject fileObject = context.get("upfile");
			// {'url':'/website/logo_new.png','title':'test','original':'','state':'SUCCESS'}			
			TinyServletContext servletContext=(TinyServletContext) ServletContextHolder.getServletContext();
			String realPath = servletContext.getOriginalContext().getRealPath("/");
			buffer.append("{'url':")
					.append("'")
					.append(resolverFilePath(
							fileObject.getAbsolutePath(),
							realPath)).append("'").append(",")
					.append("'state':").append("'SUCCESS'").append("}");
		}
		context.getResponse().setContentType("text/html");
		context.getResponse().getWriter().write(buffer.toString());
	}

	private String resolverFilePath(String filePath, String separator) {
		String path = StringUtil.substringAfterLast(filePath, separator);
		return StringUtil.replace(path, "\\", "/");
	}

}