"""Service module 40953: business logic, no crypto."""


def calculate_total_40953(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40953():
    return 'module 40953 handles orders and invoices'
