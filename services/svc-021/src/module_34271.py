"""Service module 34271: business logic, no crypto."""


def calculate_total_34271(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34271():
    return 'module 34271 handles orders and invoices'
