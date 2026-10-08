"""Service module 27447: business logic, no crypto."""


def calculate_total_27447(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27447():
    return 'module 27447 handles orders and invoices'
