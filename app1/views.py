from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import Users, Entry, Party, Agent, Transport, Viewer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def login(request):
    login_page_path = 'templates/login.html'
    if request.user.is_authenticated:
        data = request.session.get("login_user_data")
        if data:
            return redirect("dashboard")
    if request.method == 'POST':
        data = request.POST
        registration_id = data['registration_id']
        password = data['password']
        user = auth.authenticate(username=registration_id, password=password)
        if user is not None:
            # custom_user_object = Users.objects.get(user=user)
            # if not str(designation) == custom_user_object.designation:
            #     return render(request, login_page_path, {'msg': f'No {designation} with this credentials!'})
            request.session["login_user_data"] = request.POST
            auth.login(request, user)
            return redirect("dashboard")
        return render(request, login_page_path, {'msg': 'Invalid Credentials!'})
    return render(request, login_page_path)


def dashboard(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def add_transport(request):
    if request.method == 'POST':
        name = request.POST['name']
        check = Transport.objects.get(name=name)
        if (check):
            return render(request, "templates/entry.html")
        Transport.objects.create(name=name)
        return render(request, "templates/entry.html")


def add_viewer(request):
    if request.method == 'POST':
        name = request.POST['name']
        check = Viewer.objects.get(name=name)
        if (check):
            return render(request, "templates/entry.html")
        Viewer.objects.create(name=name)
        return render(request, "templates/entry.html")


def add_party(request):
    add_party_path = "templates/add_party.html"
    if request.method == 'POST':
        try:
            data = request.POST
            first_name = data['first_name']
            last_name = data['last_name']
            gst = data['gst']
            phone = data['phone']
            address = data['address']
            outstanding_balance = data['outstanding_balance']
            outstanding_brokerage = data['outstanding_brokerage']
            Party.objects.create(first_name=first_name, last_name=last_name, gst=gst, phone=phone, address=address,
                                 outstanding_balance=outstanding_balance, outstanding_brokerage=outstanding_brokerage)
            return redirect("add_party")
        except Exception as e:
            return render(request, add_party_path, {'msg': [f'User already exists..!!{e}']})
    return render(request, add_party_path)


def add_agent(request):
    add_agent_path = "templates/add_agent.html"
    if request.method == 'POST':
        try:
            data = request.POST
            first_name = data['first_name']
            last_name = data['last_name']
            gst = data['gst']
            phone = data['phone']
            address = data['address']
            outstanding_balance = data['outstanding_balance']
            outstanding_brokerage = data['outstanding_brokerage']
            Agent.objects.create(first_name=first_name, last_name=last_name, gst=gst, phone=phone, address=address,
                                 outstanding_balance=outstanding_balance)
            return redirect("add_agent")
        except Exception as e:
            return render(request, add_agent_path, {'msg': [f'User already exists..!!{e}']})
    return render(request, add_agent_path)


def add_entry(request):
    entry_page_path = 'templates/entry.html'
    if request.user.is_authenticated:
        party_list2 = Party.objects.all()
        party_list = []
        for party in party_list2:
            party_list.append(party.first_name+" " +
                              party.last_name+" " + party.gst)
        agent_list2 = Agent.objects.all()
        agent_list = []
        for agent in agent_list2:
            agent_list.append(agent.first_name+" " +
                              agent.last_name+" "+agent.gst)
        transport_list2 = Transport.objects.all()
        transport_list = []
        for transport in transport_list2:
            transport_list.append(transport.name)
        viewer_list2 = Viewer.objects.all()
        viewer_list = []
        for viewer in viewer_list2:
            viewer_list.append(viewer.name)
        if request.method == 'POST':
            data = request.POST
            e_from = data['e_from']
            e_from = e_from.split()[2]
            e_to = data['e_to']
            e_to = e_to.split()[2]
            agent2 = None if data['agent2'] == '' else data['agent2']
            if agent2 != None:
                agent2 = agent2.split()[2]
            quality = data['quality']
            quantity = data['quantity']
            metrics = data['metrics']
            rate = data['rate']
            amount = data['amount']
            transport_name = data['transport_name']
            lr_no = data['lr_no']
            viewer_name = data['viewer_name']
            # mode = data['mode']
            outstanding_date = data['outstanding_date']
            brokerage_amount_agent = 2 if (agent2 == None) else 1
            brokerage_amount_agent = brokerage_amount_agent*amount/100
            brokerage_amount_agent2 = 0 if (
                agent2 == None) else brokerage_amount_agent
            e_from = Party.objects.get(gst=e_from)
            e_to = Party.objects.get(gst=e_to)
            agent2 = Party.objects.get(gst=agent2)
            Entry.objects.create(e_from=e_from, e_to=e_to, agent2=agent2, quality=quality, quantity=quantity,
                                 metrics=metrics, rate=rate, amount=amount, outstanding_date=outstanding_date,
                                 brokerage_amount_agent=brokerage_amount_agent, brokerage_amount_agent2=brokerage_amount_agent2,
                                 clear_date=None, transport_name=transport_name, lr_no=lr_no, viewer_name=viewer_name)
        return render(request, entry_page_path, {"party_list": party_list, "agent_list": agent_list, "transport_list": transport_list, "viewer_list": viewer_list})

    return redirect("login")


def logout(request):
    auth.logout(request)
    return redirect("login")
