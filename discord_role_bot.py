@commands.command()
async def IverifY(ctx, user: discord.Member):
        print("yo")
        role = discord.utils.get(ctx.guild.roles, name="human")
        await user.add_roles(role)
        print("ye")
    