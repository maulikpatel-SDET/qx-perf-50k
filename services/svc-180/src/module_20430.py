"""Service module 20430: business logic, no crypto."""


def calculate_total_20430(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20430():
    return 'module 20430 handles orders and invoices'
