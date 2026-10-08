"""Service module 19953: business logic, no crypto."""


def calculate_total_19953(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19953():
    return 'module 19953 handles orders and invoices'
