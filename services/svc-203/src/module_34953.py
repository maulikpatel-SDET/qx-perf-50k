"""Service module 34953: business logic, no crypto."""


def calculate_total_34953(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34953():
    return 'module 34953 handles orders and invoices'
