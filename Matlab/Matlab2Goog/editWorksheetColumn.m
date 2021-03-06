function editWorksheetColumn(spreadSheetKey,workSheetKey,column,rowNumbers,cellValues,aToken)

%

% column - which column to edit
% rowNumbers - which rows to edit, eg if rowNumbers=[2 4 6] then the following cells will be edited (2,column), (4,column), (6,column)
% cellValues - the values that will be placed in the cells specified by rowNumbers entries and column

import java.io.*;
import java.net.*;
import java.lang.*;
com.mathworks.mlwidgets.html.HTMLPrefs.setProxySettings

MAXITER=20;
success=false;

safeguard=0;
nEntries = length(rowNumbers);

while (~success && safeguard<MAXITER)
    safeguard=safeguard+1;
    
    % Get edit details
    % return-empty set so that empty cells are also included
    urlCell=['https://spreadsheets.google.com/feeds/cells/' spreadSheetKey '/' workSheetKey '/private/full?return-empty=true&min-row=' num2str(min(rowNumbers)) '&max-row=' num2str(max(rowNumbers)) '&min-col=' num2str(column) '&max-col=' num2str(column)];
    con = urlreadwrite(mfilename,urlCell);
    con.setInstanceFollowRedirects(false);
    con.setRequestMethod( 'GET' );
    con.setDoInput( true );
    con.setRequestProperty('Content-Type','application/atom+xml;charset=UTF-8');
    con.setRequestProperty('Authorization',['Bearer ' aToken]);
    if (con.getResponseCode()~=200)
        con.disconnect();
        continue;
    end
    
    xmlData=xmlread(con.getInputStream());
    con.disconnect(); clear con;
    
    getURLStringList=strcat('https://spreadsheets.google.com/feeds/cells/',spreadSheetKey,'/',workSheetKey,'/private/full/batch');
    con = urlreadwrite(mfilename,getURLStringList);
    con.setInstanceFollowRedirects(false);
    con.setRequestMethod('POST');
    con.setDoOutput( true );
    con.setRequestProperty('Content-Type','application/atom+xml;charset=UTF-8');
    con.setRequestProperty('Authorization',['Bearer ' aToken]);
    
    % generate the batch requests
    event = '';
    event=['<feed xmlns=''http://www.w3.org/2005/Atom'' ' ...
        'xmlns:batch=''http://schemas.google.com/gdata/batch'' ' ...
        'xmlns:gs=''http://schemas.google.com/spreadsheets/2006''>' ...
        strcat('<id>https://spreadsheets.google.com/feeds/cells/',spreadSheetKey,'/',workSheetKey,'/private/full/</id>')];
    
    for i=1:nEntries
        editKey=xmlData.getElementsByTagName('entry').item(rowNumbers(i)-min(rowNumbers)).getElementsByTagName('link').item(1).getAttribute('href').toCharArray';
        slashIdx = strfind(editKey,'/');
        editKey=editKey((max(slashIdx)+1):end);
        
        event = [event '<entry>' ...
            strcat('<batch:id>R',num2str(rowNumbers(i)),'C',num2str(column),'</batch:id>')...
            '<batch:operation type=''update''/>'...
            strcat('<id>https://spreadsheets.google.com/feeds/cells/',spreadSheetKey,'/',workSheetKey,'/private/full/R',num2str(rowNumbers(i)),'C',num2str(column),'</id>')...
            '<link rel=''edit'' type=''application/atom+xml'' '...
            strcat(' href=''https://spreadsheets.google.com/feeds/cells/',spreadSheetKey,'/',workSheetKey,'/private/full/R',num2str(rowNumbers(i)),'C',num2str(column),'/',editKey,'''/>')...
            strcat('<gs:cell row=''',num2str(rowNumbers(i)),''' col=''',num2str(column),''' inputValue=''',cellValues{i},'''/>')...
            '</entry>'];
    end
    event = [event '</feed>'];
    
    ps = PrintStream(con.getOutputStream());
    ps.print(event);
    ps.close(); clear ps;
    if (con.getResponseCode()~=200)
        con.disconnect();
        continue;
    end
    success=true;
end
if success
    con.disconnect(); clear con;
else
    display(['Last response was: ' num2str(con.getResponseCode) '/' con.getResponseMessage().toCharArray()']);
    clear con;
    return;
end
