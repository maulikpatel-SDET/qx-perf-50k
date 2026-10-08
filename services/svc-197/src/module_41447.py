"""Service module 41447: business logic, no crypto."""


def calculate_total_41447(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41447():
    return 'module 41447 handles orders and invoices'
