import discord
import os
from discord.channel import CategoryChannel
from discord.ext import commands
from discord.utils import find, get

# Following code loads the .env file located
# Can be commented out if the user wishes to use there own token
# just be sure to assign TOKEN your token value
from dotenv import load_dotenv
from dotenv.main import find_dotenv
load_dotenv(find_dotenv())
TOKEN = os.environ.get("DISCORD_TOKEN")

COUNT = 0
# This line sets the prefix for any user activatable commands
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents = intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

'''This command prints out the judging list to the channel when called. 
This is to help the teams gthe order in which they will be called'''
@bot.command()
async def order(ctx):

    # first deletes the command made by the admin
    await ctx.message.delete()

    # channel for admin use
    channel = bot.get_channel(1060056031620780102)


    guild = ctx.guild
    # role = ctx.guild.roles
    # Finds the required roles needed in the guild
    global inperson, online
    inperson = discord.utils.find(lambda r: r.name == 'In-Person', ctx.message.guild.roles)
    online = discord.utils.find(lambda r: r.name == 'Online', ctx.message.guild.roles)
    
    # finding all the teams that were created by the participant (team creation bot created teams with a particuar colour)
    teams_str = [role.name for role in guild.roles if role.colour == discord.Colour(0x808080) ]
    # print(teams_str)

    # initiating numbering for the teams
    index = 1


    # initiating a dictionary that would be used when we need to call the next team up for judging
    global dic, V, I, online_dic, inperson_dic, online_dic_list, inperson_dic_list

    online_dic = {}
    inperson_dic = {}
    dic = {}
    V = online.name
    I = inperson.name


    if ctx.message.channel.name == "judging":

        # creating the online list
        await ctx.send('**This is the list for the teams presenting**')
        # printing the list for admin more nicely
        await channel.send('**This is the list for the teams presenting**')
        for order, team in enumerate(teams_str):
            
            # using the string names to find the roles and store them in a list
            teams_role = find(lambda r: r.name == f'{team}', ctx.message.guild.roles)
            print(teams_role)

            ONLINE = []
            INPERSON = []
            # if gthere are no memebers in team
            if len(teams_role.members) == 0:
                pass
            else:
                for member in teams_role.members:
                    # checks if member is online
                    if (online in member.roles):
                        ONLINE.append(member.name)
                        dic[f'{team}'] = V
                        print(f'{team} : {dic[team]}')
                        # sending the list to the channel
                        await ctx.send(f'{index}. {team}')
                        index += 1
                        # printing the list for admin more nicely
                        await channel.send(f'{team} : {dic[team]}')
                        continue
                    elif (inperson in member.roles):
                        INPERSON.append(member.name)   
                    else:
                        pass
            
                # checking if all members of the team are inperson
                # if they are then the team is presenting INPERSON
                if (len(INPERSON) == len(teams_role.members)):
                    # adding the teams to the dictionary                    
                    if (member.name in INPERSON):
                        dic[f'{team}'] = I
                        print(f'{team} : {dic[team]}')
                        # sending the list to the channel
                        await ctx.send(f'{index}. {team}')
                        index += 1
                        # printing the list for admin more nicely
                        await channel.send(f'{team} : {dic[team]}')                        
                        continue            

        await ctx.send('** **')
        print(dic)
        #############################################################################################################################################

        # # creating the inperson list
        # await ctx.send('**This is the list for the teams presenting inperson**')
        # # printing the list for admin more nicely
        # await channel.send('** **')
        # await channel.send('**This is the list for the teams presenting inperson**')
        # for order, team in enumerate(teams_str):
            
        #     # using the string names to find the roles and store them in a list
        #     teams_role = find(lambda r: r.name == f'{team}', ctx.message.guild.roles)
        #     # print(teams_role)

        #     INPERSON = []
        #     if len(teams_role.members) == 0:
        #         pass
        #     else:
        #         for member in teams_role.members:
        #             # checks if member is inperson
        #             if (inperson in member.roles):
        #                 INPERSON.append(member.name)
                        
        #             else:
        #                 pass
                
        #         # checking if all members of the team are inperson
        #         if (len(INPERSON) == len(teams_role.members)):
        #             # adding the teams to the dictionary                    
        #             if (member.name in INPERSON):
        #                 inperson_dic[f'{in_index}'] = f'{team}'
        #                 # sending the list to the channel
        #                 await ctx.send(f'{in_index}. {team}')
        #                 # printing the list for admin more nicely
        #                 await channel.send(f'{in_index}. {team}')

        #             #incrementing the index for the next team
        #             in_index += 1    

        # await ctx.send('** **')
        ########################################################################################################################################

        # # creating the Servus-award list
        # await ctx.send('**This is the list for the teams presenting for the Servus award**')
        # # printing the list for admin more nicely
        # await channel.send('** **')
        # await channel.send('**This is the list for the teams presenting for the Servus award**')
        # for order, team in enumerate(teams_str):
            
        #     # using the string names to find the roles and store them in a list
        #     teams_role = find(lambda r: r.name == f'{team}', ctx.message.guild.roles)
        #     # print(teams_role)

        #     Servus = []
        #     if len(teams_role.members) == 0:
        #         pass
        #     else:
        #         for member in teams_role.members:
        #             # checks if member is inperson
        #             if (Servus_award in member.roles):
        #                 Servus.append(member.name)
                        
        #             else:
        #                 pass
                
        #         # checking if all members of the team are inperson
        #         if (len(Servus) == len(teams_role.members)):
        #             # adding the teams to the dictionary                    
        #             if (member.name in Servus):
        #                 Servus_dic[f'{in_index}'] = f'{team}'
        #                 # sending the list to the channel
        #                 await ctx.send(f'{in_index}. {team}')
        #                 # printing the list for admin more nicely
        #                 await channel.send(f'{in_index}. {team}')

        #             #incrementing the index for the next team
        #             in_index += 1
        
        
        # print(inperson_dic)
        # print(online_dic)
        # print(Servus_dic)

        # # telling the teams first in both lines to get ready
        # online_dic_list = list(online_dic)
        # inperson_dic_list = list(inperson_dic)
        # Servus_dic_list = list(Servus_dic)
#################################################################################################################################################################################################################################################
        # if len(online_dic) >= 5:
        #     first_online = find(lambda r: r.name == f'{online_dic[online_dic_list[0]]}', ctx.message.guild.roles)
        #     second_online = find (lambda r: r.name == f'{online_dic[online_dic_list[1]]}', ctx.message.guild.roles)
        #     third_online = find (lambda r: r.name == f'{online_dic[online_dic_list[2]]}', ctx.message.guild.roles)
        #     # fourth_online = find (lambda r: r.name == f'{online_dic[online_dic_list[3]]}', ctx.message.guild.roles)
        #     # fifth_online = find (lambda r: r.name == f'{online_dic[online_dic_list[4]]}', ctx.message.guild.roles)
        #     await ctx.send('** **')
        #     await ctx.send(f'Hey {first_online.mention}, your team is up next for judging, so get ready. Please head to the Judging waiting room 1 voice channel and wait till you are called up next. You will automatically be transferred to the Judging Room 1.')
        #     await ctx.send(f'Hey {second_online.mention}, your team is up next for judging, so get ready. Please head to the Judging waiting room 2 voice channel and wait till you are called up next. You will automatically be transferred to the Judging Room 2.')
        #     await ctx.send(f'Hey {third_online.mention}, your team is up next for judging, so get ready. Please head to the Judging waiting room 3 voice channel and wait till you are called up next. You will automatically be transferred to the Judging Room 3.')
        #     # await ctx.send(f'Hey {fourth_online.mention}, your team is up next for judging, so get ready. Please head to the Judging waiting room 2 voice channel and wait till you are called up next. You will automatically be transferred to the Judging Room 2.')
        #     # await ctx.send(f'Hey {fifth_online.mention}, your team is up next for judging, so get ready. Please head to the Judging waiting room 2 voice channel and wait till you are called up next. You will automatically be transferred to the Judging Room 2.')
        # elif len(online_dic) == 4:
        #     first_online = find(lambda r: r.name == f'{online_dic[online_dic_list[0]]}', ctx.message.guild.roles)
        #     second_online = find (lambda r: r.name == f'{online_dic[online_dic_list[1]]}', ctx.message.guild.roles)
        #     third_online = find (lambda r: r.name == f'{online_dic[online_dic_list[2]]}', ctx.message.guild.roles)
        #     # fourth_online = find (lambda r: r.name == f'{online_dic[online_dic_list[3]]}', ctx.message.guild.roles)
        #     await ctx.send('** **')
        #     await ctx.send(f'Hey {first_online.mention}, your team is up next for judging, so get ready. Please head to the Judging waiting room 1 voice channel and wait till you are called up next. You will automatically be transferred to the Judging Room 1.')
        #     await ctx.send(f'Hey {second_online.mention}, your team is up next for judging, so get ready. Please head to the Judging waiting room 2 voice channel and wait till you are called up next. You will automatically be transferred to the Judging Room 2.')
        #     await ctx.send(f'Hey {third_online.mention}, your team is up next for judging, so get ready. Please head to the Judging waiting room 3 voice channel and wait till you are called up next. You will automatically be transferred to the Judging Room 3.')
        #     # await ctx.send(f'Hey {fourth_online.mention}, your team is up next for judging, so get ready. Please head to the Judging waiting room 2 voice channel and wait till you are called up next. You will automatically be transferred to the Judging Room 2.')
        # elif len(online_dic) == 3:
        #     first_online = find(lambda r: r.name == f'{online_dic[online_dic_list[0]]}', ctx.message.guild.roles)
        #     second_online = find (lambda r: r.name == f'{online_dic[online_dic_list[1]]}', ctx.message.guild.roles)
        #     third_online = find (lambda r: r.name == f'{online_dic[online_dic_list[2]]}', ctx.message.guild.roles)
        #     await ctx.send('** **')
        #     await ctx.send(f'Hey {first_online.mention}, your team is up next for judging, so get ready. Please head to the Judging waiting room 1 voice channel and wait till you are called up next. You will automatically be transferred to the Judging Room 1.')
        #     await ctx.send(f'Hey {second_online.mention}, your team is up next for judging, so get ready. Please head to the Judging waiting room 2 voice channel and wait till you are called up next. You will automatically be transferred to the Judging Room 2.')
        #     await ctx.send(f'Hey {third_online.mention}, your team is up next for judging, so get ready. Please head to the Judging waiting room 3 voice channel and wait till you are called up next. You will automatically be transferred to the Judging Room 3.')
        # elif len(online_dic) == 2:
        #     first_online = find(lambda r: r.name == f'{online_dic[online_dic_list[0]]}', ctx.message.guild.roles)
        #     second_online = find (lambda r: r.name == f'{online_dic[online_dic_list[1]]}', ctx.message.guild.roles)
        #     await ctx.send('** **')
        #     await ctx.send(f'Hey {first_online.mention}, your team is up next for judging, so get ready. Please head to the Judging waiting room 1 voice channel and wait till you are called up next. You will automatically be transferred to the Judging Room 1.')
        #     await ctx.send(f'Hey {second_online.mention}, your team is up next for judging, so get ready. Please head to the Judging waiting room 2 voice channel and wait till you are called up next. You will automatically be transferred to the Judging Room 2.')


        # if len(inperson_dic) >= 3:
        #     first_inperson = find(lambda r: r.name == f'{inperson_dic[inperson_dic_list[0]]}', ctx.message.guild.roles)
        #     second_inperson = find(lambda r: r.name == f'{inperson_dic[inperson_dic_list[1]]}', ctx.message.guild.roles)
        #     # third_inperson = find(lambda r: r.name == f'{inperson_dic[inperson_dic_list[2]]}', ctx.message.guild.roles)
        #     await ctx.send('** **')
        #     await ctx.send(f'Hey {first_inperson.mention}, your team is up next for judging, so get ready. Please head to the front desk.')
        #     await ctx.send(f'Hey {second_inperson.mention}, your team is up next for judging, so get ready. Please head to the front desk.')
        #     # await ctx.send(f'Hey {third_inperson.mention}, your team is up next for judging, so get ready. Please head to the front desk.')
        # elif len(inperson_dic) == 2:
        #     first_inperson = find(lambda r: r.name == f'{inperson_dic[inperson_dic_list[0]]}', ctx.message.guild.roles)
        #     second_inperson = find(lambda r: r.name == f'{inperson_dic[inperson_dic_list[1]]}', ctx.message.guild.roles)
        #     await ctx.send('** **')
        #     await ctx.send(f'Hey {first_inperson.mention}, your team is up next for judging, so get ready. Please head to the front desk.')
        #     await ctx.send(f'Hey {second_inperson.mention}, your team is up next for judging, so get ready. Please head to the front desk.')
        # elif len(inperson_dic) == 1:
        #     first_inperson = find(lambda r: r.name == f'{inperson_dic[inperson_dic_list[0]]}', ctx.message.guild.roles)
        #     await ctx.send('** **')
        #     await ctx.send(f'Hey {first_inperson.mention}, your team is up next for judging, so get ready. Please head to the front desk.')
        
        # # if len(Servus_dic) >= 1:
        # #     first_Servus = find(lambda r: r.name == f'{Servus_dic[Servus_dic_list[0]]}', ctx.message.guild.roles)
        # #     await ctx.send('** **')
        # #     await ctx.send(f'Hey {first_Servus.mention}, your team is up next for judging for the Servus award, so get ready. Please head to the Servus award judging room. You will automatically be moved')

    return dic

@bot.command()
async def move(ctx, channel: discord.VoiceChannel, *members:discord.Member):
    for member in members:
        for everymember in member:
            await everymember.move_to(channel)


@bot.command()
async def next1(ctx):

    if ctx.message.channel.name == "judging":
    
        # first deletes the command made by the admin
        await ctx.message.delete()
        
        await ctx.send('**************************************************************')
        guild = ctx.guild
        role = ctx.guild.roles
        global dic_list
        dic_list = list(dic)

        await ctx.send('** **')
        if len(dic) == 0:
            await ctx.send('There are no more teams to judge')

        elif len(dic) == 1:
            current_key = dic_list[0]
            role_name = find(lambda r: r.name == f'{current_key}', ctx.message.guild.roles)
            judging = get(ctx.guild.roles, name = 'Judgable1')

            # checking if the team is online or inperson
            if dic[current_key] == I:
                await ctx.send(f'Hey {role_name.mention}, your team will be judged now, Please head to Room 1. The Organizers at the front desk will be happy to guide where it is if you need help locating the room. You have 3 minutes to get there before you are skipped over.')
            elif dic[current_key] == V:
                members = role_name.members
                for member in members:
                    await member.add_roles(judging)
                await ctx.send(f'Hey {role_name.mention}, your team will be judged now, you have been given the judgable role so now please head over to Judging Room 1. The judges will wait up till two minutes, if you are not in online room by then you will NOT be judged and the next team will be called, thus disqualifying you. {next_role_name.mention} please get ready')

                # await ctx.send(f'Hey {role_name.mention}, your team will be judged now, you will be transferred to the Judging Room Channel 1')
                # channel = discord.utils.get(guild.voice_channels, name = "Judging Room 1")
                # await move(ctx, channel, members)

            # removes first item (team) since that team has been judged
            dic.pop(current_key)

        elif len(dic) >= 2:
            current_key = dic_list[0]
            next_key = dic_list[1]
            role_name = find(lambda r: r.name == f'{current_key}', ctx.message.guild.roles)
            next_role_name = find(lambda r: r.name == f'{next_key}', ctx.message.guild.roles)
            judging = get(ctx.guild.roles, name = 'Judgable1')

            # checking if the team is online or inperson
            if dic[current_key] == I:
                await ctx.send(f'Hey {role_name.mention}, your team will be judged now, Please head to Room 1. The Organizers at the front desk will be happy to guide where it is if you need help locating the room. You have 3 minutes to get there before you are skipped over.')
                await ctx.send(f'{next_role_name.mention} please get ready.')
            elif dic[current_key] == V:
                members = role_name.members
                for member in members:
                    await member.add_roles(judging)
                await ctx.send(f'Hey {role_name.mention}, your team will be judged now, you have been given the judgable role so now please head over to Judging Room 1. The judges will wait up till two minutes, if you are not in online room by then you will NOT be judged and the next team will be called, thus disqualifying you. {next_role_name.mention} please get ready')

                # await ctx.send(f'Hey {role_name.mention}, your team will be judged now, you will be transferred to the Judging Room Channel 1')
                # channel = discord.utils.get(guild.voice_channels, name = "Judging Room 1")
                # await move(ctx, channel, members)

            # removes first item (team) since that team has been judged
            dic.pop(current_key)

        else:
            pass
        print()
        print(f'whats left: {dic}')
        print()

    return dic
    

@bot.command()
async def next2(ctx):

    if ctx.message.channel.name == "judging":

        # first deletes the command made by the admin
        await ctx.message.delete()
        
        await ctx.send('**************************************************************')
        guild = ctx.guild
        role = ctx.guild.roles
        global dic_list
        dic_list = list(dic)

        await ctx.send('** **')
        if len(dic) == 0:
            await ctx.send('There are no more teams to judge')

        elif len(dic) == 1:
            current_key = dic_list[0]
            role_name = find(lambda r: r.name == f'{current_key}', ctx.message.guild.roles)
            judging = get(ctx.guild.roles, name = 'Judgable2')

            # checking if the team is online or inperson
            if dic[current_key] == I:
                await ctx.send(f'Hey {role_name.mention}, your team will be judged now, Please head to Room 2. The Organizers at the front desk will be happy to guide where it is if you need help locating the room. You have 3 minutes to get there before you are skipped over.')
            elif dic[current_key] == V:
                members = role_name.members
                for member in members:
                    await member.add_roles(judging)
                await ctx.send(f'Hey {role_name.mention}, your team will be judged now, you have been given the judgable role so now please head over to Judging Room 2. The judges will wait up till two minutes, if you are not in online room by then you will NOT be judged and the next team will be called, thus disqualifying you. {next_role_name.mention} please get ready')

                # await ctx.send(f'Hey {role_name.mention}, your team will be judged now, you will be transferred to the Judging Room Channel 1')
                # channel = discord.utils.get(guild.voice_channels, name = "Judging Room 1")
                # await move(ctx, channel, members)

            # removes first item (team) since that team has been judged
            dic.pop(current_key)

        elif len(dic) >= 2:
            current_key = dic_list[0]
            next_key = dic_list[1]
            role_name = find(lambda r: r.name == f'{current_key}', ctx.message.guild.roles)
            next_role_name = find(lambda r: r.name == f'{next_key}', ctx.message.guild.roles)
            judging = get(ctx.guild.roles, name = 'Judgable2')

            # checking if the team is online or inperson
            if dic[current_key] == I:
                await ctx.send(f'Hey {role_name.mention}, your team will be judged now, Please head to Room 2. The Organizers at the front desk will be happy to guide where it is if you need help locating the room. You have 3 minutes to get there before you are skipped over.')
                await ctx.send(f'{next_role_name.mention} please get ready.')
            elif dic[current_key] == V:
                members = role_name.members
                for member in members:
                    await member.add_roles(judging)
                await ctx.send(f'Hey {role_name.mention}, your team will be judged now, you have been given the judgable role so now please head over to Judging Room 2. The judges will wait up till two minutes, if you are not in online room by then you will NOT be judged and the next team will be called, thus disqualifying you. {next_role_name.mention} please get ready')

                # await ctx.send(f'Hey {role_name.mention}, your team will be judged now, you will be transferred to the Judging Room Channel 1')
                # channel = discord.utils.get(guild.voice_channels, name = "Judging Room 1")
                # await move(ctx, channel, members)

            # removes first item (team) since that team has been judged
            dic.pop(current_key)

        else:
            pass
        print()
        print(f'whats left: {dic}')
        print()

    return dic

@bot.command()
async def next3(ctx):

    if ctx.message.channel.name == "judging":

        # first deletes the command made by the admin
        await ctx.message.delete()
        
        await ctx.send('**************************************************************')
        guild = ctx.guild
        role = ctx.guild.roles
        global dic_list
        dic_list = list(dic)

        await ctx.send('** **')
        if len(dic) == 0:
            await ctx.send('There are no more teams to judge')

        elif len(dic) == 1:
            current_key = dic_list[0]
            role_name = find(lambda r: r.name == f'{current_key}', ctx.message.guild.roles)
            judging = get(ctx.guild.roles, name = 'Judgable3')

            # checking if the team is online or inperson
            if dic[current_key] == I:
                await ctx.send(f'Hey {role_name.mention}, your team will be judged now, Please head to Room 3. The Organizers at the front desk will be happy to guide where it is if you need help locating the room. You have 3 minutes to get there before you are skipped over.')
            elif dic[current_key] == V:
                members = role_name.members
                for member in members:
                    await member.add_roles(judging)
                await ctx.send(f'Hey {role_name.mention}, your team will be judged now, you have been given the judgable role so now please head over to Judging Room 3. The judges will wait up till two minutes, if you are not in online room by then you will NOT be judged and the next team will be called, thus disqualifying you. {next_role_name.mention} please get ready')

                # await ctx.send(f'Hey {role_name.mention}, your team will be judged now, you will be transferred to the Judging Room Channel 1')
                # channel = discord.utils.get(guild.voice_channels, name = "Judging Room 1")
                # await move(ctx, channel, members)

            # removes first item (team) since that team has been judged
            dic.pop(current_key)

        elif len(dic) >= 2:
            current_key = dic_list[0]
            next_key = dic_list[1]
            role_name = find(lambda r: r.name == f'{current_key}', ctx.message.guild.roles)
            next_role_name = find(lambda r: r.name == f'{next_key}', ctx.message.guild.roles)
            judging = get(ctx.guild.roles, name = 'Judgable3')

            # checking if the team is online or inperson
            if dic[current_key] == I:
                await ctx.send(f'Hey {role_name.mention}, your team will be judged now, Please head to Room 3. The Organizers at the front desk will be happy to guide where it is if you need help locating the room. You have 3 minutes to get there before you are skipped over.')
                await ctx.send(f'{next_role_name.mention} please get ready.')
            elif dic[current_key] == V:
                members = role_name.members
                for member in members:
                    await member.add_roles(judging)
                await ctx.send(f'Hey {role_name.mention}, your team will be judged now, you have been given the judgable role so now please head over to Judging Room 3. The judges will wait up till two minutes, if you are not in online room by then you will NOT be judged and the next team will be called, thus disqualifying you. {next_role_name.mention} please get ready')

                # await ctx.send(f'Hey {role_name.mention}, your team will be judged now, you will be transferred to the Judging Room Channel 1')
                # channel = discord.utils.get(guild.voice_channels, name = "Judging Room 1")
                # await move(ctx, channel, members)

            # removes first item (team) since that team has been judged
            dic.pop(current_key)
        else:
            pass
        print()
        print(f'whats left: {dic}')
        print()

    return dic

@bot.command()
async def nextI(ctx):

    if ctx.message.channel.name == "judging":

        # first deletes the command made by the admin
        await ctx.message.delete()
        
        await ctx.send('**************************************************************')
        guild = ctx.guild
        role = ctx.guild.roles
        global dic_list
        dic_list = list(dic)

        await ctx.send('** **')
        if len(dic) == 0:
            await ctx.send('There are no more teams to judge')

        elif len(dic) == 1:
            current_key = dic_list[0]
            role_name = find(lambda r: r.name == f'{current_key}', ctx.message.guild.roles)
            judging = get(ctx.guild.roles, name = 'Judgable4')

            # checking if the team is online or inperson
            if dic[current_key] == I:
                await ctx.send(f'Hey {role_name.mention}, your team will be judged now, Please head to Room 4. The Organizers at the front desk will be happy to guide where it is if you need help locating the room. You have 3 minutes to get there before you are skipped over.')
            elif dic[current_key] == V:
                members = role_name.members
                for member in members:
                    await member.add_roles(judging)
                await ctx.send(f'Hey {role_name.mention}, your team will be judged now, you have been given the judgable role so now please head over to Judging Room 4. The judges will wait up till two minutes, if you are not in online room by then you will NOT be judged and the next team will be called, thus disqualifying you. {next_role_name.mention} please get ready')

                # await ctx.send(f'Hey {role_name.mention}, your team will be judged now, you will be transferred to the Judging Room Channel 1')
                # channel = discord.utils.get(guild.voice_channels, name = "Judging Room 1")
                # await move(ctx, channel, members)

            # removes first item (team) since that team has been judged
            dic.pop(current_key)

        elif len(dic) >= 2:
            current_key = dic_list[0]
            next_key = dic_list[1]
            role_name = find(lambda r: r.name == f'{current_key}', ctx.message.guild.roles)
            next_role_name = find(lambda r: r.name == f'{next_key}', ctx.message.guild.roles)
            judging = get(ctx.guild.roles, name = 'Judgable4')

            # checking if the team is online or inperson
            if dic[current_key] == I:
                await ctx.send(f'Hey {role_name.mention}, your team will be judged now, Please head to Room 4. The Organizers at the front desk will be happy to guide where it is if you need help locating the room. You have 3 minutes to get there before you are skipped over.')
                await ctx.send(f'{next_role_name.mention} please get ready.')
            elif dic[current_key] == V:
                members = role_name.members
                for member in members:
                    await member.add_roles(judging)
                await ctx.send(f'Hey {role_name.mention}, your team will be judged now, you have been given the judgable role so now please head over to Judging Room 4. The judges will wait up till two minutes, if you are not in online room by then you will NOT be judged and the next team will be called, thus disqualifying you. {next_role_name.mention} please get ready')

                # await ctx.send(f'Hey {role_name.mention}, your team will be judged now, you will be transferred to the Judging Room Channel 1')
                # channel = discord.utils.get(guild.voice_channels, name = "Judging Room 1")
                # await move(ctx, channel, members)

            # removes first item (team) since that team has been judged
            dic.pop(current_key)
        else:
            pass
        print()
        print(f'whats left: {dic}')
        print()

    return dic



bot.run(TOKEN)