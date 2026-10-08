"""Service module 31953: business logic, no crypto."""


def calculate_total_31953(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31953():
    return 'module 31953 handles orders and invoices'
