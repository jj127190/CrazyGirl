package org.tinygroup.uiupload;

import java.io.File;
import java.text.SimpleDateFormat;
import java.util.Date;

import javax.servlet.http.HttpServletRequest;

import org.tinygroup.commons.tools.UUID;
import org.tinygroup.weblayer.listener.ServletContextHolder;
import org.tinygroup.weblayer.listener.TinyServletContext;
import org.tinygroup.weblayer.webcontext.parser.upload.FileUploadReName;

public class UmRename implements FileUploadReName {
	
	private File repository;

	public String reName(String localFileName, HttpServletRequest request) {
		UUID uuid = new UUID();
		String UID = uuid.nextID().replace(':', '_').replace('-', '_');
		TinyServletContext servletContext=(TinyServletContext) ServletContextHolder.getServletContext();
		String realPath = servletContext.getOriginalContext().getRealPath("/");
		String dayString=fmtDateToStr(new Date(), "yyyy-MM-dd");
		File catalog=new File(realPath + "/upload/image/"+dayString+"/");
		if(!catalog.exists()){
			catalog.mkdirs();
		}
		return catalog.getPath()+"/"+ UID + localFileName.substring(localFileName.lastIndexOf("."));
	}
	
	public static String fmtDateToStr(Date date, String dtFormat) {  
        if (date == null){
        	date=new Date();
        }
        try {  
            SimpleDateFormat dateFormat = new SimpleDateFormat(dtFormat);  
            return dateFormat.format(date);  
        } catch (Exception e) {  
        }  
        return null;
    }

	public void setRepository(File repository) {
		this.repository=repository;
	}

	public File getRepository() {
		return repository;
	}  

}
