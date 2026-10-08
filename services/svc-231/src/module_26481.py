"""Service module 26481: business logic, no crypto."""


def calculate_total_26481(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26481():
    return 'module 26481 handles orders and invoices'
