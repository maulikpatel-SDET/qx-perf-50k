"""Service module 6953: business logic, no crypto."""


def calculate_total_6953(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6953():
    return 'module 6953 handles orders and invoices'
