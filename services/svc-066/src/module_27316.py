"""Service module 27316: business logic, no crypto."""


def calculate_total_27316(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27316():
    return 'module 27316 handles orders and invoices'
