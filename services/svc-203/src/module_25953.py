"""Service module 25953: business logic, no crypto."""


def calculate_total_25953(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25953():
    return 'module 25953 handles orders and invoices'
