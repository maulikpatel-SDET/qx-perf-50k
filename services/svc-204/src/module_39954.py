"""Service module 39954: business logic, no crypto."""


def calculate_total_39954(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39954():
    return 'module 39954 handles orders and invoices'
