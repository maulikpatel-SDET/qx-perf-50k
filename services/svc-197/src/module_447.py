"""Service module 447: business logic, no crypto."""


def calculate_total_447(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_447():
    return 'module 447 handles orders and invoices'
