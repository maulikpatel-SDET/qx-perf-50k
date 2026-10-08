"""Service module 17953: business logic, no crypto."""


def calculate_total_17953(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17953():
    return 'module 17953 handles orders and invoices'
