"""Service module 13953: business logic, no crypto."""


def calculate_total_13953(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13953():
    return 'module 13953 handles orders and invoices'
