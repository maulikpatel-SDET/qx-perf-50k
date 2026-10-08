"""Service module 11447: business logic, no crypto."""


def calculate_total_11447(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11447():
    return 'module 11447 handles orders and invoices'
