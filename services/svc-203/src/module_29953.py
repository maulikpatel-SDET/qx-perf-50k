"""Service module 29953: business logic, no crypto."""


def calculate_total_29953(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29953():
    return 'module 29953 handles orders and invoices'
