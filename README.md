# quizz3
   
   მოცემული პროგრამა ეფუძნება openweathermap-ის 5 day weather forecast მოდულს. ინფორმაცია მომაქვს შესაბამის აპიდან და ვბეჭდავ გარკვეულ ინფორმაციას requests მოდულის
რამოდენიმე ფუნქცია/ატრიბუტის გამოყენებით.
   json ფორმატის მონაცემბეს json ფაილში ვინახავ სტრუქტურული სახით. res ცვლადში ვინახავ json-ის ლექსიკონს(dictionary).

   შემდეგ ვბეჭდავ ინფორმაციას res ლექსიკონიდან: ტემპერატურის, წნევის, ზღვის დონის, ტენიანობის შესახებ და აგრეთვე ამინდის მოკლე აღწერას მაგ. კრიალა ცა, მსუბუქი წვიმა, ღუბლიანი ცა  და ა.შ. გარდა ამისა ვბეჭდავ შესაბამის თარიღს შემდეგი ფორმატით: წელი-თვე-დღე საათი:წუთი:წამი. არსებულ ინფორმაციას ვწერ sqlite-ის ბაზაში და აგრეთვე ბაზიდან წამოღებულ მონაცემებს ვბეჭდავ კონსოლში. 


# 5 day weather forecast აპი
   
   მოცემული აპიდან ინფორმაციის წამოღება შესაძლებელია კონკრეტული ქალაქის დასახელების მითითებით url-ში. დაბრუნებულ json-ში ინფორმაცია ინახება მითითებული ქალაქის ამინდის
პროგნოზის შესახებ ხუთი დღის მანძილზე სამ-სამი საათის ინტერვალით. აგრეთვე დროის მიხედვით წერია ინფორმაცია ტენიანობის, წნევის, ქარის და სხვა მრავალი მონაციემის შესახებ.
გარდა ამისა ინფორმაცია მოყვება ქალაქის პოპულაცისს, დროითი სარტყელის, ქვეყნის კოდის შესახებ და ა.შ.    
